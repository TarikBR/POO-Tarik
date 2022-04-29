class Voo:
    def __init__(self, numVoo, data):
        self.numVoo = numVoo
        self.data = data
        self.ocupacao = []
        for i in range(100):
            self.ocupacao.append(False)

    def proximoLivre(self):
        for i in range(len(self.ocupacao)):
            if not self.ocupacao[i]:
                print(f'O próximo assento livre é {i + 1}.')
                break

    def verifica(self, numAssento):
        if not self.ocupacao[numAssento + 1]:
            print('O assento esta livre.')
        else:
            print('O assento já esta ocupado.')

    def ocupa(self, numAssento):
        if not self.ocupacao[numAssento - 1]:
            self.ocupacao[numAssento - 1] = True
            print('Operação foi bem sucedida.')
        else:
            print('O assento já esta ocupado.')

    def vagas(self):
        livres = 0
        for i in range(len(self.ocupacao)):
            if not self.ocupacao[i]:
                livres += 1
        print(f'O total de vagas livres é {livres}.')

    def getVoo(self):
        print(f'O número do Vôo é {self.numVoo}.')
