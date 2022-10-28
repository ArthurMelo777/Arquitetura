from comAsm import *
from convnum import *
from manipulTXT import *

# TESTES

asm = Asm('')
mTxt = Arquivo()
comandos = mTxt.tratarArray()
linhashexa = []

for i in range(len(comandos)):
    asm.defCode(comandos[i])
    asm.criaArray()
    asm.atribReg()
    asm.convs()
    c = binToHex(asm.retBinario())
    c.converter()
    linhashexa.append(c.retHex())

mTxt.escreverArquivo(linhashexa)