# Capítulo 8 · Respostas comentadas

[← Perguntas](8.5-contexto-e-diagnostico.md#pare-e-explique) · [Índice do capítulo](README.md)

As respostas retomam o percurso e as condições declaradas. Os testes executados pertencem aos exemplos próprios; não demonstram o funcionamento de qualquer programa desconhecido.

## 1. Fonte e artefato são objetos distintos

A edição mudou o fonte, não o executável que já havia sido construído. Sem reconstrução automática ou manual, iniciar o mesmo artefato anterior preserva seu cálculo. Depois de reconstruir com o fonte alterado, o novo programa apresenta nove. O diagnóstico deve identificar qual versão foi editada, construída e executada, em vez de concluir que a CPU somou errado.

## 2. Declaração não fornece necessariamente uma definição

A declaração apresenta nome, parâmetros e tipo de retorno. O corpo em `acervo.c` define as operações que implementam a função. O compilador pode aceitar a chamada conhecendo a declaração, mas a ligação ainda precisa resolver a implementação. Repetir o cabeçalho não substitui o objeto que a contém.

## 3. Quatro responsabilidades no percurso C

O pré-processador trata inclusões e outras diretivas. A compilação traduz a descrição segundo a linguagem e o alvo. A montagem produz código objeto a partir de assembly. A ligação combina peças e resolve referências. Com `-c`, o GCC produz um objeto sem a ligação final; com `-E` ou `-S`, interrompe antes, nas representações indicadas. A interface pode coordenar todas as etapas sem torná-las equivalentes.

## 4. Um formato pode descrever papéis diferentes

ELF organiza diferentes tipos de artefato. `principal.o` é relocável e participa da ligação; `catalogo` foi produzido para iniciar uma execução no ambiente considerado. É necessário ler os campos e a organização, não presumir que a presença de instruções ou da assinatura ELF torne qualquer arquivo um programa completo. Um executável independente de posição pode utilizar `ET_DYN`, portanto o teste admite essa possibilidade sem confundi-la automaticamente com uma biblioteca.

## 5. Criar e substituir não são a mesma operação

No Linux, `fork` cria um filho com identidade de processo própria. Um `execve` bem-sucedido substitui a imagem executada por um processo existente, preservando seu PID. Outros atributos seguem as regras documentadas; não se deve generalizar que nada mais muda. Nem todo lançador precisa usar exatamente esse par de interfaces.

## 6. A preparação antecede o corpo principal

Carregamento, preparação de dependências e inicialização do runtime podem acontecer antes de `main`. O ponto de entrada do executável não é automaticamente a função que o autor reconhece como início do fonte. `__libc_start_main` é um exemplo documentado dessa preparação, não um nome universal de todas as plataformas.

## 7. Interpretar não exclui compilar

CPython compila o fonte para um objeto de código com bytecode e executa essa representação por seu mecanismo. O cache `.pyc` pode conservar trabalho relativo a módulos importados, mas não é um executável nativo universal nem condição necessária para toda compilação. A implementação e sua versão determinam a representação; o rótulo da linguagem não explica o percurso inteiro.

## 8. O mesmo artefato pode receber contextos diferentes

Argumentos, variáveis de ambiente, diretório corrente, arquivos e permissões podem mudar. Bibliotecas e serviços disponíveis também participam do ambiente. Abrir `dados.txt` em duas pastas diferentes não garante acessar o mesmo objeto. Precisamos comparar as condições relevantes antes de atribuir a diferença à alteração do binário.

## 9. Resultado apresentado e código de saída

Cinco é o valor de domínio que o programa apresenta no texto. Zero é seu código de encerramento normal, escolhido pelo programa conforme uma convenção. O código zero não significa que ele imprimiu zero nem prova autorização, integridade de todos os dados ou ausência de defeitos. Precisamos conhecer o contrato do programa e quais condições ele efetivamente verificou.

[Voltar ao capítulo](README.md) · [Índice do módulo](../README.md) · [Glossário](../../glossario.md)
