# Conversor de Assembly para Hexadecimal

## Anotações

### Passos
1. Criei o conversor de binário para hexadecimal e em seguida, de decimal para binário
2. Tratei os strings para que ficassem no formato adequado "comando r1, r2, r3"
3. Verifiquei os padrões dos comandos e separei em três grupos (1 parâmetro, 3 parâmetro e 4 parâmetro)
SEPARAÇÃO DOS GRUPOS:
1 atributo - nop, syscall
3 atributos - div, divu, mult, multu
4 atributos - add, addi, addiu, addu, and, andi, mul, nor, or, ori, sll, slt, slti, sltiu, sltu, sra, srl, sub, subu, xor, xori
4. Adicionei condicionais para verificar e retornar o binário de cada comando acima citado
5. Adicionei comandos para manipulação de arquivos .txt
6. Finalizei com os comandos do main.py

### Problemas
LOOP INFINITO!!! Não consigo adicionar os zeros para completar 16 bits. (*PROBLEMA SOLUCIONADO*)
Como verificar se um comando possui dois ou três parâmetros?
Como realizar o comando nop?
Comandos com imediate, como posso realizar o split?