The Open John Language
PT-BR
(V0.1)

Olá querido(a) leitor(a),
Desde já agradeço por você estar lendo essa documentação! Se você está aqui significa que você decidiu testar o JL, ou simplesmente conhecer meu projeto,
Isso é um grande motivo para eu me alegrar.
Obrigado!

Escrito Por: João Victor


! Isso é um comentário  
I.0-Introdução:
I.1- O que é a oJl?

oJl (Open John Language) é uma linguagem de programação desenvolvida com o propósito de ser clara, simples e acessível. Sua sintaxe foi projetada para se aproximar de uma linguagem natural, facilitando a leitura e compreensão do código, o que a torna adequada tanto para iniciantes quanto para desenvolvedores experientes que buscam produtividade.
! Como seu nome diz oJl é um projeto de código aberto, sinta-se à vontade para modificar estudar a fundo como o projeto funciona.
O principal objetivo da oJl é ser intuitiva e funcional, sem abrir mão da eficiência. Trata-se de um projeto experimental em constante evolução, com a meta de oferecer uma alternativa viável e amigável no ecossistema de linguagens de programação.
A oJl é disponibilizada como software de código aberto, permitindo que a comunidade contribua livremente com melhorias, adição de recursos e adaptações específicas às suas necessidades. A única exigência é a manutenção dos créditos ao criador original.
Em essência, a oJl não é apenas uma linguagem, mas sim uma ferramenta que busca ser uma parceira do programador, simplificando o processo de desenvolvimento sem comprometer a utilidade e a robustez.

I.2- Porque eu criei a oJl?

As linguagens de programação são ferramentas fundamentais que nos permitem nos comunicar com as máquinas desde o século XX. Hoje existem inúmeras opções, cada uma com sua proposta, mas a maioria delas apresenta uma sintaxe complexa, que pode ser desafiadora tanto para iniciantes quanto para desenvolvedores já experientes. Embora esse processo de aprendizado faça parte da jornada, acredito que é possível seguir por outro caminho.
A oJl nasceu desse propósito: ser acolhedora, simples e funcional, permitindo que projetos complexos possam ser desenvolvidos de forma clara e acessível.
Não posso deixar de reconhecer que a criação da oJl também surgiu de uma motivação pessoal: o desejo de construir algo que tivesse identidade própria e pudesse ser reconhecido. Sempre admirei as linguagens já existentes e suas marcas visuais, e essa inspiração, somada à minha paixão por design e logomarcas, me levou a idealizar a oJl. Mesmo que venha a ser lembrada como uma linguagem “diferente” ou até “estranha”, para mim, o mais importante é que ela carregue personalidade e significado.
A oJl é, portanto, tanto um projeto técnico quanto criativo, que busca unir simplicidade, identidade e inovação em uma única linguagem.


I.3- Objetivos da linguagem

Como mencionado anteriormente, a JL foi desenvolvida com o objetivo de ser fácil de aprender e utilizar. Mas surge a pergunta: em quais projetos a linguagem pode ser aplicada?
A oJl foi projetada para ter um foco geral, podendo ser utilizada em diferentes tipos de projetos, desde os mais simples até aplicações mais complexas. Embora ainda esteja em fase inicial e apresente certas limitações, sua proposta de ser uma linguagem aberta e flexível permite que qualquer pessoa adapte, expanda e crie novas versões de acordo com suas próprias necessidades e objetivos.
Em resumo, a oJl busca ser uma linguagem versátil, que pode evoluir junto com sua comunidade, tornando-se cada vez mais útil e adequada a diferentes cenários de desenvolvimento.

P.0 - Primeiros Passos:
P.1 - Como Instalar?
A instalação da JL é rápida e simples. Basta baixar o interpretador disponível no site oficial do projeto.	
A JL foi desenvolvida em Python, portanto, é necessário ter o Python instalado em sua máquina.
Após isso, siga os passos:
> Baixe o interpretador
 Faça o download do arquivo ojlreader.py.


> Crie seu arquivo JL
 Crie um arquivo com a extensão .ojl (por exemplo: meu_codigo.ojl).


> Execute seu programa
 Para rodar o arquivo, basta abrir o interpretador com o Python, passando o arquivo como argumento:

 python3 ojlreader.py meu_codigo.ojl

Pronto! Agora você já pode escrever e executar seus primeiros programas na oJl.
! Também não posso ignorar o fato de que executar programas escritos em oJl é um processo chato, irei começar a trabalhar em uma IDE, para que seja algo mais fácil de se trabalhar.










P.2 - Requisitos do sistema
A JL foi desenvolvida para ser leve e acessível, podendo ser executada em praticamente qualquer dispositivo que ofereça suporte à instalação de programas.
Requisitos mínimos
> Qualquer sistema operacional capaz de executar Python 3.8 ou superior


> Editor de texto para criação de arquivos .ojl


> Terminal ou prompt de comando para execução dos programas


Observações
> A JL não exige hardware avançado e pode rodar em computadores simples ou ambientes virtuais.


> Por ser uma linguagem experimental e de código aberto, sua compatibilidade pode ser ampliada conforme a comunidade contribui com o projeto.











P.3 - Seu primeiro programa
Agora que a JL está instalada, podemos criar o primeiro programa. Tradicionalmente, toda linguagem de programação inicia com o clássico “Hello, World!”, e aqui não será diferente.
1. Criar um arquivo JL
Abra um editor de texto de sua preferência e salve o arquivo com a extensão .ojl.
 Exemplo: hello.ojl.
2. Escrever o código
No interior do arquivo, insira a seguinte linha:
say "Hello, World!";

O comando say ; é responsável por exibir mensagens, desempenhando um papel semelhante ao print em outras linguagens de programação.
3. Executar o programa
No terminal, utilize o interpretador para executar o arquivo criado:
python3 lexer.py hello.ojl

4. Resultado esperado
Caso tudo tenha sido configurado corretamente, o programa exibirá a seguinte saída:
Hello, World!
 
M.0 - O Manual
M.1 - Sintaxe
A sintaxe da oJl busca ser simples, e compreensível, se assemelhando como se fosse uma conversa. A sintaxe da oJl foi evoluindo com o tempo e sendo mais e mais polida, para ficar mais “clean”, mais simples, algo que não seja muito assustador, oJl busca ser prático.
! Por curiosidade vou mostrar a evolução da sintaxe da linguagem, antes o projeto começou com uma sintaxe um pouco estranha, a ideia era ser como se fosse o “Scratch de texto”, oJl funcionava com blocos, aqui vai um simples “Hello World”:
when_tcs{       < Bloco “when” com a extensão “tcs” significa “the code start”, é meio explicativo “quando o código começar… ” acredito fortemente que seja uma ideia boa, só que quanto menos coisas melhor correto?
 	say = “Hello World”       < Diga “Hello World”   
}       < Fechamento do bloco
Decidi mudar pois parece uma linguagem meio “poluída” é claro oJl já teve muitas modificações e identidades, mas foi sendo modificada para facilidade e simplicidade.
A oJl tem um manual simples,  para explicar suas funcionalidades e capacidade até o momento, aqui está “a bíblia oJl” o seu manual que irá explicar como desenvolver seus códigos, O manual se encontra no próximo tópico.
M.2 - A bíblia oJl

M.2.1. Comentários

Comentários são usados para adicionar notas ao código que o interpretador ignora. Em OJL, qualquer texto após um ponto de exclamação `!` é considerado um comentário.

! Este é um comentário de linha inteira.
var nome = "John"; ! Isto é um comentário no final da linha.



M.2.2. Variáveis

Variáveis são usadas para armazenar dados. A OJL suporta números e texto (strings).

> Declaração
Use a palavra-chave `var`.

! Declarando uma variável de texto
var mensagem = "Olá, mundo!";

! Declarando uma variável numérica
var idade = 25;

> Uso
Para usar o valor de uma variável, coloque um cifrão `$` antes do nome dela.

say $mensagem;

M.2.3. Comando `say` (Saída)

O comando `say` é usado para imprimir valores na tela. Ele pode imprimir texto literal ou o valor de variáveis.

say "Este é um texto literal.";
say $idade;





M.2.4. Comando `calc` (Cálculos)

O comando `calc` realiza uma operação matemática e armazena o resultado em uma variável. A sintaxe é `calc [expressão] -> [variável_destino];`.

- Suporta as 4 operações básicas: `+`, `-`, `*`, `/`.
- Suporta apenas uma operação por vez.
- Os nomes das variáveis na expressão não precisam do `$`.

var x = 10;
var y = 5;
var resultado = 0;

calc x + y -> resultado; ! resultado agora contém 15
say $resultado;

M.2.5. Estruturas de Controle (Comando `if`)

O comando `if` executa um bloco de código somente se uma condição for verdadeira. 

IMPORTANTE: O comando `if` inteiro, incluindo sua condição e corpo, deve estar em uma única linha.

- A condição usa um único sinal de igual `=` para comparação.
- O corpo do `if` é definido entre parênteses `()`.

var nota = 10;
if $nota = 10 (say "Parabéns, nota máxima!";);

M.2.6. Funções

Funções permitem agrupar código para ser reutilizado.

IMPORTANTE: A definição da função inteira deve estar em uma única linha.

> Definição
A sintaxe é `f nome_da_funcao (corpo_da_funcao);`.

f saudacao (say "Olá!";say "Bem-vindo à OJL!";);

> Chamada
Para executar uma função, a sintaxe é `f nome_da_funcao;`.

f saudacao;


M.3 - Precisa de ajuda?
	
	Encontrou algum erro? Quer dizer alguma sugestão? 
https://docs.google.com/forms/d/e/1FAIpQLSeLlWwxam5vtrnn6Onjt6RYGyQ-1BeLNBIVEg8ArTUKQCI94g/viewform?usp=header
Diga aqui.

F.0 - Considerações finais

	
Chegamos ao fim dessa documentação, caso algo tenha sido mal explicado, ou faltou alguma explicação, ou se você ainda possui dúvidas, não exite em perguntar!
	Fico feliz em saber que você chegou até esse ponto, espero que essa documentação por mais simples que seja possa ser útil para você. Espero que a oJl seja um projeto bom para as pessoas, estou disponível a ouvir suas ideias para que esse projeto seja um projeto incrível para todos, nos acompanhe no GitHub para mais informações.

Obrigado! ;D


oJl é um projeto de código aberto criado por João Victor.
Versão documentação: oJl Biblie V0.1 PT-BR
Versão atual oJl: betaV0.1
Página github: https://github.com/ojlang
Minha página: https://github.com/PernilongoKiller 
