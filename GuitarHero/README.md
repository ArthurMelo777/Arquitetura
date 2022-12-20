# Projeto de Arquitetura de Computadores
## Guitar Hero 4 bit (tela 512x256)
1. Para jogar, faça o download do Mars 4.5, disponível em: https://drive.google.com/file/d/1bDiW40e8NAa9rSw_EKw2VwsTk15AacNk/view
2. Abra o arquivo "main.asm" e execute :)

## Processo de criação
### Musica
Para criar a música no Assembly Mars, utilizei o syscall code "31", especificado na própria documentação do programa. Contei com a ajuda ainda do meu amigo e músico Lucas Henrique, que me auxiliou com as notas da música por mim escolhida: Smoke on the water - Deep Purple

### Cenário
Para a criação do cenário, utilizei a estratégia do meu veterano de curso Lucas Gabriel, que consiste em simular todo o cenário no excel, com os blocos de cores contendo seu respectivo código hexadecimal. Logo em seguida, criei no arquivo "cenario.asm" 64 vetores onde ocupei todos com os códigos de cada linha, preenchidos anteriomente no Excel.  
Criei então, agora no arquivo "main.asm", um código que armazena dois endereços de memória em dois registradores distintos. O primeiro registrador ($8) irá exibir na tela as cores antes armazenadas no arquivo contendo o cenário, enquanto que o segundo ($24) irá fazer uma cópia das cores para, caso no futuro haja alguma mudança (movimento do cenário), seja possível recuperar as cores.

*NOTA* O número de vetores é referente à divisão do tamanho da tela por o número de bits utilizado (256/4 = 64). 