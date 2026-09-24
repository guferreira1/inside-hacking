#!/usr/bin/env python3
"""Check the Markdown/link conventions used by this book; no network access.

This deliberately validates our Markdown subset, not every extension of GFM.
External URLs are inventoried, not declared healthy or fact-checked.
"""
from __future__ import annotations
import argparse
import html
import json
import re
import sys
import unicodedata
from collections import Counter
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit


class HTMLLinks(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = set()

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        for key in ('href', 'src'):
            if attrs.get(key):
                self.links.append(attrs[key])
        for key in ('id', 'name'):
            if attrs.get(key):
                self.ids.add(attrs[key])


def prose(text):
    text = re.sub(r'<!--.*?-->', '', text, flags=re.S)
    out, marker, size = [], None, 0
    for line in text.splitlines():
        fence = re.match(r'^\s{0,3}(`{3,}|~{3,})', line)
        if fence:
            token = fence.group(1)
            if marker is None:
                marker, size = token[0], len(token)
            elif token[0] == marker and len(token) >= size:
                marker = None
            continue
        if marker is None:
            out.append(line)
    return '\n'.join(out)


def slug(value):
    value = re.sub(r'\[([^]]+)\]\([^)]*\)', r'\1', value)
    value = html.unescape(re.sub(r'<[^>]*>', '', value)).strip().lower()
    return ''.join(c for c in value if c in ' _-' or unicodedata.category(c)[0] in 'LNM').replace(' ', '-')


def parse(text):
    clean = prose(text)
    parser = HTMLLinks()
    parser.feed(clean)
    ids, used, titles = set(parser.ids), Counter(), []
    for line in clean.splitlines():
        match = re.match(r'^ {0,3}#{1,6}\s+(.+?)(?:\s+#+\s*)?$', line)
        if match:
            title = match.group(1)
            base = slug(title)
            anchor = base if not used[base] else f'{base}-{used[base]}'
            while anchor in ids:
                used[base] += 1
                anchor = f'{base}-{used[base]}'
            ids.add(anchor)
            used[base] += 1
            titles.append(title)
    visible = re.sub(r'(`+).*?\1', '', clean)
    links = list(parser.links)
    inline = r'!?\[[^\]]*\]\((<[^>]+>|[^\s()]+(?:\([^()]*\)[^\s()]*)*)(?:\s+[\"\'][^\n]*?[\"\'])?\)'
    links += [m.group(1).strip('<>') for m in re.finditer(inline, visible)]
    definitions = {}
    for m in re.finditer(r'^ {0,3}\[([^\]^][^\]]*)\]:\s*<?(\S+?)>?(?:\s+[\"\'].*)?$', visible, re.M):
        definitions[m.group(1).lower()] = m.group(2)
    for m in re.finditer(r'!?\[([^\]]+)\]\[([^\]]*)\]', visible):
        label = (m.group(2) or m.group(1)).lower()
        links.append(definitions.get(label, 'MISSING-REFERENCE:' + label))
    for m in re.finditer(r'https?://[^\s<>\"\']+', visible):
        value = m.group(0).rstrip('.,;')
        while value.endswith(')') and value.count(')') > value.count('('):
            value = value[:-1]
        links.append(value)
    return {'links': list(dict.fromkeys(links)), 'ids': ids, 'titles': titles, 'clean': clean}


def audit(root):
    files = sorted(p for p in root.rglob('*.md') if '.git' not in p.relative_to(root).parts)
    docs = {p.resolve(): parse(p.read_text(encoding='utf-8')) for p in files}
    errors, external, internal, inventory = [], {}, 0, []
    for path, doc in docs.items():
        rel = path.relative_to(root).as_posix()
        for raw in doc['links']:
            url = html.unescape(raw)
            if url.startswith('MISSING-REFERENCE:'):
                errors.append({'file': rel, 'link': url, 'problem': 'undefined reference'})
                continue
            parts = urlsplit(url)
            if parts.scheme or parts.netloc:
                if parts.scheme in ('http', 'https'):
                    external.setdefault(url, []).append(rel)
                continue
            internal += 1
            target = (root / unquote(parts.path).lstrip('/')) if parts.path.startswith('/') else (path.parent / unquote(parts.path))
            if not parts.path:
                target = path
            target = target.resolve()
            try:
                target.relative_to(root)
            except ValueError:
                errors.append({'file': rel, 'link': raw, 'problem': 'escapes repository'})
                continue
            if not target.exists():
                errors.append({'file': rel, 'link': raw, 'problem': 'missing target'})
                continue
            if parts.fragment:
                if target.is_dir():
                    target = target / 'README.md'
                anchors = docs.get(target, {}).get('ids')
                if anchors is not None and unquote(parts.fragment) not in anchors:
                    errors.append({'file': rel, 'link': raw, 'problem': 'missing anchor'})
        caps = sorted(set(re.findall(r'(?<![\w])(?:[A-Z][A-Z0-9/-]{1,}|[A-Za-z]+(?:[A-Z][a-z]+)+)(?![\w])', doc['clean'])))
        statuses = [line for line in doc['clean'].splitlines() if '**Status:**' in line]
        inventory.append({'file': rel, 'headings': len(doc['titles']), 'links': len(doc['links']), 'status': statuses, 'acronyms': caps})
    return {'markdown_files': len(files), 'internal_links': internal, 'internal_errors': errors, 'external_urls': external, 'inventory': inventory, 'glossary_entries': sum(1 for line in (root/'book/glossario.md').read_text(encoding='utf-8').splitlines() if line.startswith('### ')) if (root/'book/glossario.md').exists() else 0}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path('.'))
    parser.add_argument('--inventory', action='store_true')
    args = parser.parse_args()
    try:
        result = audit(args.root.resolve())
    except (OSError, ValueError, UnicodeError) as exc:
        print(f'Cannot audit documentation: {exc}', file=sys.stderr)
        return 2
    if not args.inventory:
        result.pop('inventory')
        result['external_urls'] = len(result['external_urls'])
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 1 if result['internal_errors'] else 0


if __name__ == '__main__':
    sys.exit(main())
