from convnum import decToBin

class Asm ():
    def __init__ (self, code, lcode='', t=0, r1='0', r2='0', r3='0', s=''):
        self.code = code
    
    def imediate (self):
        if self.lcode[0] == 'addi' or self.lcode[0] == 'addiu' or self.lcode[0] == 'andi' or self.lcode[0] == 'ori' or self.lcode[0] == 'slti' or self.lcode[0] == 'sltiu' or self.lcode[0] == 'sll' or self.lcode[0] == 'sra' or self.lcode[0] == 'srl' or self.lcode[0] == 'xori':
            return True
        else: return False

    def criaArray (self):
        self.lcode = self.code.split(' ')
        if self.imediate():
            self.lcode[1], self.lcode[2] = self.lcode[1][1:], self.lcode[2][1:]
        else:
            self.lcode[1], self.lcode[2], self.lcode[3] = self.lcode[1][1:], self.lcode[2][1:], self.lcode[3][1:]
        self.t = len(self.lcode)
    
    def atribReg (self):
        if self.t == 3:
            self.r1, self.r2 = self.lcode[1], self.lcode[2]
        elif self.t == 4:
            self.r1, self.r2, self.r3 = self.lcode[1], self.lcode[2], self.lcode[3]

    def convs (self):
        cd1, cd2, cd3 = decToBin(self.r1), decToBin(self.r2), decToBin(self.r3)
        cd1.converter(), cd2.converter(), cd3.converter()
        cd1.regBit(), cd2.regBit(), cd3.regBit()
        self.r1, self.r2, self.r3 = cd1.retBin(), cd2.retBin(), cd3.retBin()

    def verificarTamanho (self):
        if len(self.s) == 32: return True
        else: return False

    def repararTamanho (self):
        while not self.verificarTamanho():
            tamR1, tamR2, tamR3 = len(self.r1), len(self.r2), len(self.r3)

            if self.verificarTamanho(): break

            if tamR3 == 5: self.r3 = '00000000000' + self.r3
            if tamR3 == 6: self.r3 = '0000000000' + self.r3
            if tamR3 == 7: self.r3 = '000000000' + self.r3
            if tamR3 == 8: self.r3 = '00000000' + self.r3
            if tamR3 == 9: self.r3 = '0000000' + self.r3
            if tamR3 == 10: self.r3 = '000000' + self.r3
            if tamR3 == 11: self.r3 = '00000' + self.r3
            if tamR3 == 12: self.r3 = '0000' + self.r3
            if tamR3 == 13: self.r3 = '000' + self.r3
            if tamR3 == 14: self.r3 = '00' + self.r3
            if tamR3 == 15: self.r3 = '0' + self.r3

            return self.r3

    def retBinario (self):
        if self.lcode[0] == 'add':
            self.s = '000000' + self.r2 + self.r3 + self.r1 + '00000' + '100000'
            return self.s
        if self.lcode[0] == 'addi':
            self.s = '001000' + self.r2 + self.r1 + self.r3
            self.s = '001000' + self.r2 + self.r1 + self.repararTamanho()
            return self.s