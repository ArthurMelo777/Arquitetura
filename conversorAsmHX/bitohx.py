class biToHex:
    def __init__(self, bi, hx = ''):
        self.bi = bi
        self.hx = hx
    
    def numHex(self, n):
        if n == 10: return "A"
        elif n == 11: return "B"
        elif n == 12: return "C"
        elif n == 13: return "D"
        elif n == 14: return "E"
        elif n == 15: return "F"

    def converter (self):
        bif = ['', '', '', '', '', '', '', ''] # numeros separados 4 a 4
        b1, b2, b3, b4 = -4, -3, -2, -1
        for i in range(8):
            b1, b2, b3, b4 = b1+4, b2+4, b3+4, b4+4
            bif[i] = int(self.bi[b1])*8 + int(self.bi[b2])*4 + int(self.bi[b3])*2 + int(self.bi[b4])*1
        
        for i in range(8):
            if bif[i] >= 10: bif[i] = self.numHex(bif[i])
            self.hx = self.hx + f'{bif[i]}'
        
        return self.hx