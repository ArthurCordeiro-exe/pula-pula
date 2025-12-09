from src.crianca import Crianca


class PulaPula:

    def __init__(self, limiteMax):
        self.limiteMax = limiteMax
        self.criancadentro = []
        self.filaespera = []
        self.caixa = 0
        self.conta = dict()

    def getFilaDeEspera(self):
        return self.filaespera

    def getCriancasPulando(self):
        return self.criancadentro

    def getLimiteMax(self):
        return self.limiteMax

    def getCaixa(self):
        return self.caixa

    def getConta(self, nome):
        for i in self.conta.keys():
            if nome == i.getNome():
                return self.conta[i]
        return None


    def entrarNaFila(self, crianca: Crianca):
        for i in range(len(self.filaespera)):
            if crianca.getNome() in self.filaespera[i].getNome():
                return False
        self.filaespera.append(crianca)
        return True


    def entrar(self):
        if len(self.filaespera) > 0:
            if len(self.criancadentro) < self.getLimiteMax():
                crianca = self.filaespera[0]
                self.criancadentro.insert(0, crianca)
                self.filaespera.pop(0)
                for nomes in self.criancadentro:
                    if nomes not in self.conta:
                        self.conta[nomes] = 2.5
                    else:
                        self.conta[nomes] = self.conta[nomes] + 2.5
                return True
            return False
        return False

    def sair(self):
        if len(self.criancadentro) > 0:
            crianca = self.criancadentro[-1]
            self.filaespera.append(crianca)
            self.criancadentro.pop(-1)
            return True
        return False

    def papaiChegou(self, nome):
        for i in range(len(self.criancadentro)):
            if nome == self.criancadentro[i].getNome():
                for chaves in self.conta:
                    if chaves.getNome() == nome:
                        conta = self.conta[chaves]
                        self.caixa += conta
                self.criancadentro.pop(i)
                return True
        for e in range(len(self.filaespera)):
            if nome == self.filaespera[e].getNome():
                for chaves in self.conta:
                    if chaves.getNome() == nome:
                        conta2 = self.conta[chaves]
                        self.caixa += conta2
                self.filaespera.pop(e)
                return True
        return False

    def fechar(self):
        for chaves in self.conta:
            self.caixa += self.conta[chaves]
            self.conta[chaves] = None
        self.criancadentro = []
        self.filaespera = []
        return True