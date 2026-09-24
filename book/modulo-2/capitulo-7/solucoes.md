# Capítulo 7 · Respostas comentadas

[← Perguntas](7.5-dispositivos-e-firmware.md#pare-e-explique) · [Índice do capítulo](README.md)

As respostas retomam modelos e premissas do texto. Não descrevem um diagnóstico executado no computador do leitor.

## 1. Apresentação e persistência

A apresentação demonstra que existiu um estado suficiente para produzir a tela. O enunciado exclui salvamento automático e recuperação, e a nova versão ainda não foi gravada de forma persistente. Ela pode existir em memória volátil sem que o arquivo armazenado tenha mudado. Não se deve generalizar o comportamento para todos os editores.

## 2. Diferentes lugares, diferentes funções

Registradores guardam valores utilizados diretamente na execução do processador. A RAM oferece uma área de trabalho maior. O armazenamento persistente conserva arquivos sem alimentação contínua. Um resultado num registrador ainda precisa participar das operações de escrita necessárias para preservar o documento; uma soma não salva automaticamente um arquivo.

## 3. Frequência e trabalho

Dois bilhões de ciclos por segundo correspondem a 0,5 nanossegundo por ciclo. A conta não fixa instruções por ciclo, esperas ou paralelismo. Quatro milhões de ciclos à frequência constante hipotética dariam 2 ms; isso não transforma ciclos em instruções nem é medição de uma CPU.

## 4. Contextos compartilhados

Os contextos lógicos podem compartilhar recursos do mesmo núcleo. Não duplicam toda a estrutura física. O resultado depende do trabalho e de como esses recursos são utilizados; não existe garantia geral de desempenho dobrado.

## 5. Média do modelo

`(8 × 2 + 2 × 20) / 10 = 5,6` unidades. O custo de um miss já inclui a consulta inicial: duas unidades mais dezoito adicionais. Não somamos a consulta duas vezes. Os números são premissas didáticas e omitem filas, sobreposição e outros níveis; a conta confere o modelo, não um produto real.

## 6. Endereço e contexto

Os programas podem utilizar endereços virtuais iguais com traduções físicas diferentes. Também pode haver compartilhamento autorizado. É necessário conhecer a visão de endereço e o mapeamento relevante; o número isolado não prova nenhuma das duas situações.

## 7. Comunicação e limites

O controlador gerencia operações no lado do dispositivo; o driver é software que participa da comunicação entre sistema e dispositivo. DMA permite transferências sem cópia byte a byte pela CPU principal, mas requer preparação e controle. Uma IOMMU pode restringir destinos conforme a configuração; o simples nome do recurso não demonstra que a proteção esteja ativa.

## 8. O significado da confirmação

Não necessariamente. Uma cache volátil pode reconhecer que recebeu os dados antes de eles alcançarem o meio não volátil. É preciso conhecer o contrato e os mecanismos de escoamento e confirmação. Persistência também não garante imunidade a qualquer falha física futura.

## 9. Não confundir camadas

M.2 descreve formato/conexão, enquanto NVMe descreve uma interface de comandos; existem SSDs M.2 com outras interfaces. Secure Boot participa da autorização de componentes no boot, não da prova de correção de todos os programas. Nos dois casos, uma característica foi indevidamente transformada em garantia de outra.

[Voltar ao capítulo](README.md) · [Índice do módulo](../README.md)
