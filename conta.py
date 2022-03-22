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

    def sacar(self, sacar):
        if sacar <= self._limite:
            self._saldo -= sacar
        else:
            print("Limite indisponível!")
