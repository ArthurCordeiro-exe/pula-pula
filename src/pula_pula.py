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
        if nome in self.conta:
            return self.conta[nome]
        else:
            return None


    def entrarNaFila(self, crianca: Crianca):
        if crianca.getNome() in self.filaespera:
            return False
        else:
            self.filaespera.append(crianca.getNome())
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
        conta = 0
        if nome in self.criancadentro:
            self.criancadentro.pop(self.criancadentro.index(nome))
            for chaves in self.conta:
                if chaves == nome:
                    conta = self.conta[chaves]
            self.caixa += conta
            return True
        if nome in self.filaespera:
            self.filaespera.pop(self.filaespera.index(nome))
            for chaves in self.conta:
                if chaves == nome:
                    conta = self.conta[chaves]
            self.caixa += conta
            return True
        return False

    def fechar(self):
        for chaves in self.conta:
            self.caixa += self.conta[chaves]
            self.conta[chaves] = None
        self.criancadentro = []
        self.filaespera = []
        return True