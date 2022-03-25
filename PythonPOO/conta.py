class Conta:
    def __init__(self, num, titular, saldo, limite):
        print('Construindo objeto ... {a}'.format(a=self))
        self._num = num
        self._titular = titular
        self._saldo = saldo
        self._limite = limite

    def extrato(self):
        print("saldo de {a} do titular {b}".format(a=self._saldo, b=self._titular))

    def deposita(self, valor):
        print("Depositando valor de {a} na conta do titular {b}".format(a=valor, b=self._titular))
        self._saldo += valor

    def limite(self, limite):
        print("Alterando limite de {a} para {b}".format(a=self._limite, b=limite))
        self._limite = limite

    def sacar(self, valor):
        if valor <= self._limite:
            self._saldo -= valor
            print("Sacado com sucesso! Saldo atual: {a}".format(a=self._saldo))
        else:
            print("Limite indisponível!")

    def transfere(self, valor, destino):
        self._saldo -= valor
        destino._saldo += valor
        print("Transferido com sucesso!")
