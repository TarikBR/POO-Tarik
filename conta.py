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
        self._saldo += valor

    def limite(self, limite):
        self._limite = limite

    def sacar(self, valor):
        if valor <= self._limite:
            self._saldo -= valor
        else:
            print("Limite indisponível!")

    def transfere(self, valor, destino):
        self._saldo -= valor
        destino._saldo += valor
