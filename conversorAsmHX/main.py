from comAsm import *
from convnum import *

# TESTES

a = Asm('addi $2 $0 5')
a.criaArray()
print(a.lcode)
a.atribReg()
a.convs()
v = a.retBinario()
print(v)
c = binToHex(v)
c.converter()
v = c.retHex()
print(v)
a.code = 'syscall'
a.criaArray()
print(a.lcode)
a.atribReg()
a.convs()
v = a.retBinario()
print(v)
c = binToHex(v)
c.converter()
v = c.retHex()
print(v)