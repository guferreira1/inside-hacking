#requires -Version 7.0
param(
    [AllowEmptyCollection()]
    [AllowEmptyString()]
    [string[]]$Estados = @()
)

if ($Estados.Count -lt 1 -or $Estados.Count -gt 256) {
    throw 'Forneca de 1 a 256 estados.'
}

$disponiveis = 0
$emprestados = 0

foreach ($estado in $Estados) {
    if ($estado -ceq 'disponivel') {
        $disponiveis += 1
    }
    elseif ($estado -ceq 'emprestado') {
        $emprestados += 1
    }
    else {
        throw 'Estado invalido; nenhum resumo produzido.'
    }
}

[pscustomobject]@{
    Disponiveis = $disponiveis
    Emprestados = $emprestados
}
