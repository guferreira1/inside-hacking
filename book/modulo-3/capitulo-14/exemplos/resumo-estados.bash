if (( $# == 0 || $# > 256 )); then
    printf '%s\n' 'uso: bash resumo-estados.bash ESTADO [ESTADO ...]' >&2
    exit 2
fi

disponiveis=0
emprestados=0

for estado in "$@"; do
    case "$estado" in
        disponivel) disponiveis=$((disponiveis + 1)) ;;
        emprestado) emprestados=$((emprestados + 1)) ;;
        *)
            printf '%s\n' 'estado invalido; nenhum resumo produzido' >&2
            exit 2
            ;;
    esac
done

printf 'disponiveis=%s\nemprestados=%s\n' "$disponiveis" "$emprestados"
