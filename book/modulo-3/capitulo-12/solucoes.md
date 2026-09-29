# Capítulo 12 · Respostas comentadas

[← Perguntas](12.5-pacotes-atualizacoes-e-investigacao.md#pare-e-explique) · [Índice do capítulo](README.md)

As respostas distinguem os mecanismos documentados das premissas fictícias da Aurora. Explicar a relação com suas próprias palavras é mais importante que repetir a redação.

## 1. Núcleo e composição

Linux nomeia o kernel. Debian integra esse núcleo a bibliotecas, programas, configurações e manutenção. A distribuição não é apenas uma aparência gráfica, e o kernel não contém automaticamente todos os programas instalados. Compartilhar o núcleo não demonstra igualdade de dependências ou serviços.

## 2. Uma execução e uma identificação da instalação

`uname -r` apresenta a identificação da release do kernel em execução. `os-release` identifica a instalação na visão de arquivos consultada. Kernel e distribuição têm ciclos e identificações diferentes; em contextos com kernel compartilhado, as consultas também podem descrever camadas diferentes. A divergência sozinha não prova erro nem identifica um container.

## 3. Começo da árvore, identidade e diretório pessoal

`/` é a raiz da resolução de caminhos; root é uma conta administrativa; `/root` é um caminho convencional para seu diretório pessoal. A finalidade de `/etc` ou `/var` não informa por si só a permissão de cada objeto. É necessário examinar contexto e regras, não deduzir acesso pela grafia.

## 4. Um layout previsto

Na organização merged-/usr, determinados caminhos tradicionais são links para equivalentes em `/usr`. As notas do Debian documentam essa escolha. O link não indica, por si só, arquivo ausente ou corrupção. É preciso relacionar um desenho histórico à organização adotada pela distribuição.

## 5. Visibilidade não é existência

Montar uma origem sobre um diretório muda o que uma resolução por aquele caminho alcança. O conteúdo anterior pode ficar encoberto sem ter sido apagado. Uma bind mount disponibiliza uma árvore existente em outro ponto; não produz necessariamente outra cópia dos dados. Duas rotas para o mesmo objeto não equivalem a duas versões recuperáveis independentes.

## 6. A observação tem um contexto

Processos podem estar em namespaces de montagem distintos ou utilizar bases de resolução diferentes. A consulta realizada no terminal descreve a visão de quem a executa, não automaticamente a do serviço. O diagnóstico deve identificar o processo relevante e as condições de propagação e visibilidade; não basta comparar textos de caminhos.

## 7. Entrada e destino

O exemplo observa os metadados do link em procfs e, separadamente, os do destino alcançado. A comparação com o descritor original identifica o mesmo arquivo regular naquele momento. A leitura confirma os seis bytes próprios. Isso não comprova acesso a outro processo, identidade universal de inode, segurança de isolamento ou compartilhamento da posição de leitura entre duas aberturas.

## 8. A interface não define toda a origem

Procfs apresenta estado de processos e do sistema. Sysfs organiza objetos e atributos do kernel; algumas escritas podem operar controles. Arquivos de dispositivo oferecem interfaces com contratos específicos, como o descarte em `/dev/null`. Tmpfs mantém conteúdo em memória virtual, pode usar swap e não garante persistência após reinicialização. `/tmp` é um caminho e não prova, por seu nome, o uso de tmpfs.

## 9. Etapas que não se substituem

O módulo instalado é um artefato disponível; carregado indica integração ao kernel em funcionamento. Reconhecer o dispositivo e associá-lo ao driver são outras relações. Montar seu sistema de arquivos torna conteúdo alcançável numa visão de nomes. A disponibilidade do catálogo exige relacionar essas etapas ao contexto do serviço. Um componente incorporado ao kernel também pode não aparecer na lista de módulos carregados.

## 10. Manutenção, execução e confiança

Atualizar índices consulta metadados; instalar ou atualizar pacotes modifica o estado da instalação; utilizar uma versão depende da execução efetiva. Um backport pode aplicar uma correção sem adotar toda a versão upstream mais recente, exigindo examinar a revisão completa e o aviso pertinente. A autenticação do repositório ajuda a verificar procedência e integridade sob a confiança configurada, mas não demonstra ausência de vulnerabilidades. Cada verificação responde a uma parte do problema.

[Voltar ao capítulo](README.md) · [Módulo III](../README.md) · [Glossário](../../glossario.md)
