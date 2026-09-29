# Primeira entrega editorial — Capítulo 11

**Data:** 28/09/2026. **Estado:** DRAFT 0.1. **Módulo:** III.  
**Base:** `96c60302e63223ea87e440a3e42059191302ede7`.

[Manuscrito](../../book/modulo-3/capitulo-11/README.md) · [Referências](../../book/modulo-3/capitulo-11/referencias.md) · [Exemplo](../../book/modulo-3/capitulo-11/exemplos/README.md)

## Objetivo, continuidade e recorte

Abrir o Módulo III com uma explicação integrada das responsabilidades de um sistema operacional. Cinco seções conectam abstrações, kernel e espaço de usuário, interfaces, recursos, espera, identidade, limites, inicialização e ciclo de vida de serviços. O caso fictício da Aurora acompanha o mesmo importador em contextos distintos. Dez perguntas opcionais possuem respostas comentadas.

O capítulo não substitui as unidades seguintes sobre Linux, Windows, permissões, serviços e isolamento. Capabilities, LSM, namespaces e cgroups são introduções ao papel de cada mecanismo, não guias completos de configuração. A leitura independe da execução do programa.

## Pesquisa e revisão interna da primeira entrega

Fontes S1–S14 relacionam documentação Linux, Debian, Microsoft, seL4, Python, systemd e OWASP. Foram distinguidos abstração e garantia, mecanismo e política, conta administrativa e modo kernel, tempo de CPU e duração total, identidade do serviço e identidade do cliente, visão de recursos e limitação de consumo, prontidão e capacidade de atendimento.

A documentação systemd efetivamente consultada é uma reprodução identificada no man7; tentativas aos endereços freedesktop.org não retornaram conteúdo utilizável. Uma afirmação histórica sobre o escalonador presente em sched(7) não foi generalizada para o kernel atual. A comparação de microkernel não extrapola a verificação de um componente para certificação de todo o sistema.

## Evidência executada

Seis testes locais aprovados em Linux x86-64, kernel 6.18.44, glibc 2.41, Python 3.13.5. Três tratam o programa próprio, a saída literal de uma execução independente e a limpeza da pasta temporária. Três conferem modelos de duração, autorização e dependência circular.

O script completo produziu `leitura=Livro`, `fim_da_leitura=0`, `escrita=EBADF`, `ausente=ENOENT` e `conteudo_preservado=sim`. O laço de leitura é limitado e contempla leituras parciais. EBADF é resultado de uma escrita em abertura somente de leitura, não evidência de falta de permissão de outra conta. Não houve rastreamento de chamadas, teste de privilégios, acesso a arquivos pessoais, exaustão ou criação de serviços.

O clone local do repositório falhou por resolução de rede. A suíte completa e a navegação foram verificadas separadamente na preparação da entrega, no [workflow de apoio](https://github.com/guferreira1/inside-hacking/actions/runs/36506254993): **60 testes aprovados**, **113 arquivos Markdown**, **888 destinos internos conferidos** e **nenhum erro interno detectado**. As URLs externas são inventariadas, não certificadas como acessíveis por esse passo. A validação do commit final deve ser conferida em seu próprio workflow, após a retirada dos auxiliares temporários.

## Glossário, preservação e segunda passagem

O glossário passou de **340 para 373 verbetes**, com **33 entradas novas** vinculadas a ocorrências do capítulo 11. A operação conferiu o SHA do arquivo-base e verificou que os 340 blocos originais permanecem intactos. Os novos termos incluem VFS, espaço de usuário, UID/GID, capabilities Linux, cgroup, namespace, daemon e os erros explicados no exemplo.

A atualização programática ocorreu em uma branch temporária, com alterações limitadas aos nove documentos de apoio previstos. Os scripts e o workflow usados apenas para essa edição não integram a entrega na `main`; o workflow permanente de documentação permanece inalterado. O commit final reúne manuscrito, exemplos, testes e documentação, e recebe nova checagem de conjunto antes da integração.

## Documentação e estado

README principal, índice geral, abertura do Módulo III, continuidade a partir do Módulo II e capítulo 10, bibliografia, glossário, cobertura e controle editorial acompanham a entrega. As entradas do glossário apontam para suas ocorrências; nenhum tema futuro foi importado apenas para aumentar a lista.

A solicitação desta rodada autoriza continuar a escrita. Não contém avaliação explícita da leitura do capítulo 10; seu estado anterior é preservado, sem inventar aprovação, horas ou prática. Também não foi concluída nesta entrega a revisão pendente do capítulo 1 ou a revisão de conjunto dos módulos anteriores. O capítulo 11 permanece em primeira leitura e com revisão independente pendente. Não houve geração de PDF nem publicação no LinkedIn.

**Próxima revisão:** conferir a clareza da passagem entre operação, identidade, recurso e contexto. Próximo capítulo planejado: **12 — Linux por dentro**.
