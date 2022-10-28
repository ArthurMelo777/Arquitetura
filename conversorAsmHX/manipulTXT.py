class Arquivo:
    def __init__(self, arquivoasm='', arquivohx='', primeiroArray=[],comandos=[]):
        self.arquivo = arquivoasm
        self.arquivohx = arquivohx
        self.primeiroArray = primeiroArray
        self.comandos = comandos

    def abrirArquivoLer (self):
        self.arquivoasm = open("C:/Users/meloa/Documents/Arquitetura/conversorAsmHX/arquivoASM.txt", "r")
    
    def abrirArquivoEscrever (self):
        self.arquivoasm = open("C:/Users/meloa/Documents/Arquitetura/conversorAsmHX/arquivoHX.txt", "a")

    def zerarArquivo (self):
        self.arquivohx = open("C:/Users/meloa/Documents/Arquitetura/conversorAsmHX/arquivoHX.txt", "w")
        self.arquivohx.write('')

    def tratarArray (self):
        self.lerArquivo()
        for i in range(2, len(self.primeiroArray)-1):
            self.comandos.append(self.primeiroArray[i][:-1])
        self.comandos.append(self.primeiroArray[-1])
        return self.comandos

    def lerArquivo (self):
        self.abrirArquivoLer()
        for linha in self.arquivoasm:
            self.primeiroArray.append(linha)
        self.arquivoasm.close()

    # def criarArquivo (self):
    #     self.abrirArquivo()
    #     self.arquivohx = open("conversorAsmHX/arquivoHX.txt", "x")
    #     self.fecharArquivo()

    def escreverArquivo (self, vhx):
        self.zerarArquivo()
        self.abrirArquivoEscrever()
        
        for i in range(len(vhx)):
            if i == 0: self.arquivohx.write(vhx[0])
            else: self.arquivohx.write(f'\n{vhx[i]}')
            
        self.arquivohx.close()