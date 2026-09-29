printf 'quantidade=%s\n' "$#"
for item in "$@"; do
    printf '<%s>\n' "$item"
done
