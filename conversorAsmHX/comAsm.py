from convnum import decToBin

class Asm ():
    def __init__ (self, code, lcode='', t=0, r1='0', r2='0', r3='0', s='', syscode=''):
        self.code = code
    
    def defCode(self, code):
        self.code = code
    
    def imediate (self):
        if self.lcode[0] == 'addi' or self.lcode[0] == 'addiu' or self.lcode[0] == 'andi' or self.lcode[0] == 'ori' or self.lcode[0] == 'slti' or self.lcode[0] == 'sltiu' or self.lcode[0] == 'sll' or self.lcode[0] == 'sra' or self.lcode[0] == 'srl' or self.lcode[0] == 'xori':
            return True
        else: return False

    def doisAtributos (self):
        if self.lcode[0] == 'div' or self.lcode[0] == 'divu' or self.lcode[0] == 'mult' or self.lcode[0] == 'multu':
            return True
        else: return False

    def criaArray (self):
        self.lcode = self.code.split(' ')
        if self.imediate():
            self.lcode[1], self.lcode[2] = self.lcode[1][1:], self.lcode[2][1:]
        elif self.doisAtributos():
            self.lcode[1], self.lcode[2] = self.lcode[1][1:], self.lcode[2][1:]
        elif self.code == 'syscall': pass
        else:
            self.lcode[1], self.lcode[2], self.lcode[3] = self.lcode[1][1:], self.lcode[2][1:], self.lcode[3][1:]
        self.t = len(self.lcode)
    
    def atribReg (self):
        if self.t == 3:
            self.r1, self.r2 = self.lcode[1], self.lcode[2]
        elif self.t == 4:
            self.r1, self.r2, self.r3 = self.lcode[1], self.lcode[2], self.lcode[3]

    def convs (self):
        if self.doisAtributos():
            cd1, cd2 = decToBin(self.r1), decToBin(self.r2)
            cd1.converter(), cd2.converter()
            cd1.regBit(), cd2.regBit()
            self.r1, self.r2= cd1.retBin(), cd2.retBin()
        else:
            cd1, cd2, cd3 = decToBin(self.r1), decToBin(self.r2), decToBin(self.r3)
            cd1.converter(), cd2.converter(), cd3.converter()
            cd1.regBit(), cd2.regBit(), cd3.regBit()
            self.r1, self.r2, self.r3 = cd1.retBin(), cd2.retBin(), cd3.retBin()

    def verificarTamanho (self):
        if len(self.s) == 32: return True
        else: return False

    def repararTamanho (self):
        tamR3 = len(self.r3)

        if self.verificarTamanho(): return self.r3

        if tamR3 == 5: self.r3 = '00000000000' + self.r3
        elif tamR3 == 6: self.r3 = '0000000000' + self.r3
        elif tamR3 == 7: self.r3 = '000000000' + self.r3
        elif tamR3 == 8: self.r3 = '00000000' + self.r3
        elif tamR3 == 9: self.r3 = '0000000' + self.r3
        elif tamR3 == 10: self.r3 = '000000' + self.r3
        elif tamR3 == 11: self.r3 = '00000' + self.r3
        elif tamR3 == 12: self.r3 = '0000' + self.r3
        elif tamR3 == 13: self.r3 = '000' + self.r3
        elif tamR3 == 14: self.r3 = '00' + self.r3
        elif tamR3 == 15: self.r3 = '0' + self.r3

        return self.r3
        
    # def defSyscode (self):
    #     self.syscode = self.lcode[3]
    #     sd = decToBin(self.syscode)
    #     sd.converter(), sd.regBit()
    #     self.syscode = sd.retBin()
        
    # def repararSyscode (self):
    #     tamSyscode = len(self.syscode)

    #     if self.verificarTamanho(): return self.syscode

    #     if tamSyscode == 5: self.syscode = '000000000000000' + self.syscode
    #     elif tamSyscode == 6: self.syscode = '00000000000000' + self.syscode
    #     elif tamSyscode == 7: self.syscode = '0000000000000' + self.syscode
    #     elif tamSyscode == 8: self.syscode = '000000000000' + self.syscode
    #     elif tamSyscode == 9: self.syscode = '00000000000' + self.syscode
    #     elif tamSyscode == 10: self.syscode = '0000000000' + self.syscode
    #     elif tamSyscode == 11: self.syscode = '000000000' + self.syscode
    #     elif tamSyscode == 12: self.syscode = '00000000' + self.syscode
    #     elif tamSyscode == 13: self.syscode = '0000000' + self.syscode
    #     elif tamSyscode == 14: self.syscode = '000000' + self.syscode
    #     elif tamSyscode == 15: self.syscode = '00000' + self.syscode
    #     elif tamSyscode == 16: self.syscode = '0000' + self.syscode
    #     elif tamSyscode == 17: self.syscode = '000' + self.syscode
    #     elif tamSyscode == 18: self.syscode = '00' + self.syscode
    #     elif tamSyscode == 19: self.syscode = '0' + self.syscode

    #     return self.syscode

    def retBinario (self):
        if self.lcode[0] == 'add':
            self.s = '000000' + self.r2 + self.r3 + self.r1 + '00000' + '100000'
            return self.s
        elif self.lcode[0] == 'addi':
            self.s = '001000' + self.r2 + self.r1 + self.r3
            self.s = '001000' + self.r2 + self.r1 + self.repararTamanho()
            # if self.lcode[1] == '2': self.defSyscode()
            return self.s
        elif self.lcode[0] == 'addiu':
            self.s = '001001' + self.r2 + self.r1 + self.r3
            self.s = '001001' + self.r2 + self.r1 + self.repararTamanho()
            return self.s
        elif self.lcode[0] == 'addu':
            self.s = '000000' + self.r2 + self.r3 + self.r1 + '00000' + '100001'
            return self.s
        elif self.lcode[0] == 'and':
            self.s = '000000' + self.r2 + self.r3 + self.r1 + '00000' + '100100'
            return self.s
        elif self.lcode[0] == 'andi':
            self.s = '001100' + self.r2 + self.r1 + self.r3
            self.s = '001100' + self.r2 + self.r1 + self.repararTamanho()
            return self.s
        elif self.lcode[0] == 'div':
            self.s = '000000' + self.r1 + self.r2 + '0000000000' + '011010'
            return self.s
        elif self.lcode[0] == 'divu':
            self.s = '000000' + self.r1 + self.r2 + '0000000000' + '011011'
            return self.s
        elif self.lcode[0] == 'mul':
            self.s = '011100' + self.r2 + self.r3 + self.r1 + '00000' + '000010'
            return self.s
        elif self.lcode[0] == 'mult':
            self.s = '000000' + self.r1 + self.r2 + '0000000000' + '011000'
            return self.s
        elif self.lcode[0] == 'multu':
            self.s = '000000' + self.r1 + self.r2 + '0000000000' + '011001'
            return self.s
        elif self.lcode[0] == 'nop':
            self.s = '000000' + '00000' + '00000' + '00000' + '00000' + '000000'
            return self.s
        elif self.lcode[0] == 'nor':
            self.s = '000000' + self.r2 + self.r3 + self.r1 + '00000' + '100111'
            return self.s
        elif self.lcode[0] == 'or':
            self.s = '000000' + self.r2 + self.r3 + self.r1 + '00000' + '100101'
            return self.s
        elif self.lcode[0] == 'ori':
            self.s = '001101' + self.r2 + self.r1 + self.r3
            self.s = '001101' + self.r2 + self.r1 + self.repararTamanho()
            return self.s
        elif self.lcode[0] == 'sll':
            self.s = '000000' + '00000' + self.r2 + self.r1 + self.r3 + '000000'
            return self.s
        elif self.lcode[0] == 'slt':
            self.s = '000000' + self.r2 + self.r3 + self.r1 + '00000' + '101010'
            return self.s
        elif self.lcode[0] == 'slti':
            self.s = '001010' + self.r2 + self.r1 + self.r3
            self.s = '001010' + self.r2 + self.r1 + self.repararTamanho()
            return self.s
        elif self.lcode[0] == 'sltiu':
            self.s = '001011' + self.r2 + self.r1 + self.r3
            self.s = '001011' + self.r2 + self.r1 + self.repararTamanho()
            return self.s
        elif self.lcode[0] == 'sltu':
            self.s = '000000' + self.r2 + self.r3 + self.r1 + '00000' + '101011'
            return self.s
        elif self.lcode[0] == 'sra':
            self.s = '000000' + '00000' + self.r2 + self.r1 + self.r3 + '000011'
            return self.s
        elif self.lcode[0] == 'srl':
            self.s = '000000' + '0000' + '0' + self.r2 + self.r1 + self.r3 + '000010'
            return self.s
        elif self.lcode[0] == 'sub':
            self.s = '000000' + self.r2 + self.r3 + self.r1 + '00000' + '100010'
            return self.s
        elif self.lcode[0] == 'subu':
            self.s = '000000' + self.r2 + self.r3 + self.r1 + '00000' + '100011'
            return self.s
        elif self.code == 'syscall':
            # self.s = '000000' + self.syscode + '001100'
            # self.s = '000000' + self.repararSyscode() + '001100'
            self.s = '000000' + '00000000000000000000' + '001100'
            return self.s
        elif self.lcode[0] == 'xor':
            self.s = '000000' + self.r2 + self.r3 + self.r1 + '00000' + '100110'
            return self.s
        elif self.lcode[0] == 'xori':
            self.s = '001110' + self.r2 + self.r1 + self.r3
            self.s = '001110' + self.r2 + self.r1 + self.repararTamanho()
            return self.s