#requires -Version 7.0
param(
    [AllowEmptyCollection()]
    [AllowEmptyString()]
    [string[]]$Valores = @()
)

[pscustomobject]@{
    Quantidade = $Valores.Count
    Valores = @($Valores)
}
