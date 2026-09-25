# Capítulo 9 · Respostas comentadas

[← Perguntas](9.5-protecao-concorrencia-e-diagnostico.md#pare-e-explique) · [Índice do capítulo](README.md)

As respostas retomam as premissas do texto. As contas de endereços são modelos; somente o exemplo indicado de mapeamentos foi executado. Não é necessário repetir as frases para demonstrar compreensão.

## 1. O contexto faz parte do endereço

Faltam o espaço de endereços e o mapeamento aplicado. O número virtual identifica uma posição naquela visão, não uma coordenada física universal. A e B podem usar o mesmo número com destinos diferentes; também podem compartilhar um destino sob números diferentes. Conteúdo igual não resolve essa distinção.

## 2. Organização não é isolamento

Threads POSIX do mesmo processo compartilham o espaço global e recursos como descritores. Mantêm estados de execução e pilhas próprios, mas as pilhas pertencem ao espaço do processo. Sua organização separada não cria automaticamente uma barreira contra outro thread que utilize validamente um endereço recebido. Acesso e tempo de vida continuam sujeitos às regras pertinentes.

## 3. Tradução do modelo

`0x1234 = 0x12 × 256 + 0x34`. O deslocamento é `0x34`, ou 52 bytes. Com a página mapeada ao quadro `0xA7`, o endereço físico do modelo é `0xA7 × 256 + 0x34 = 0xA734`. Os 256 bytes foram escolhidos didaticamente; não são o tamanho universal de página dos sistemas reais.

## 4. Faltas em camadas distintas

A TLB conserva traduções. Uma tradução ausente nela pode existir nas tabelas e corresponder a uma página residente. Já um page fault pode exigir preparação normal de memória, cópia na escrita, E/S ou tratamento de acesso proibido. O nome não identifica sozinho a causa e não comprova defeito de hardware.

## 5. O limite do objeto é menor

Os índices válidos do bloco de 16 bytes são 0–15. O índice 16 produz `0x4110`, fora de `[0x4100, 0x4110)`, mas ainda dentro da região maior `[0x4000, 0x5000)`. Uma checagem apenas da região não conhece automaticamente a fronteira daquele objeto. Não provocar uma interrupção não torna a escrita válida.

## 6. Três acontecimentos diferentes

O término do tempo de vida encerra a validade de uso do objeto sob seu contrato. Apagar os dados exige tratar suas representações e cópias. Reduzir RSS envolve a gestão de páginas residentes. O alocador pode conservar espaço para reutilização depois de uma liberação; não observar redução imediata não demonstra sozinho um vazamento.

## 7. Visibilidade privada e compartilhada

O filho altera duas regiões com contratos diferentes. A escrita no mapeamento privado não modifica a visão privada do pai; a do compartilhado fica visível na região comum. A espera garante que a leitura do pai ocorra após a conclusão do filho. O programa confere esses valores; não inspeciona endereços físicos ou mede a quantidade de cópias feitas pelo kernel.

## 8. Contar compartilhamento duas vezes

Cada processo associa seus 4 KiB privados aos 8 KiB compartilhados, produzindo RSS de 12 KiB. Somar os RSS conta o mesmo conteúdo compartilhado duas vezes: 24 KiB. O recorte físico único contém `4 + 4 + 8 = 16 KiB`. Dividir os 8 KiB igualmente entre os dois participantes produz PSS de 8 KiB para cada um. Esses números excluem outros custos e não são um inventário de uma máquina real.

## 9. A leitura antiga também participa do erro

Se A e B já leram cinco, serializar somente as escritas permite que ambos gravem seis. A propriedade exigida envolve ler, calcular e atualizar como uma operação lógica coordenada, ou utilizar um incremento atômico apropriado. Obter sete numa tentativa não elimina outros intercalamentos. O modelo não prevê todos os efeitos de uma data race em C, que possui regras próprias de comportamento indefinido.

## 10. Proteções com objetivos diferentes

DEP/NX restringe a execução em páginas não autorizadas para esse uso. ASLR varia a disposição de regiões, dificultando certas suposições de localização. Nenhum deles decide se o usuário A pode receber o comprovante de B. Um erro de autorização pode existir mesmo com execução e acessos de memória compatíveis com os controles da plataforma.

[Voltar ao capítulo](README.md) · [Índice do módulo](../README.md) · [Glossário](../../glossario.md)
