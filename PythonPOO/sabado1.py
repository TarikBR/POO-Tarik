class Pessoa:
    def __init__(self, nome, idade, cpf, numero, endereco):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf
        self.numero = numero
        self.endereco = endereco


    def dizerDados(self):
        print(f"Meu nome é {self.nome}, tenho {self.idade} anos, número para contato {self.numero}, moro no endereço {self.endereço}, e meu CPF é {self.cpf}")

    def caminhar(self):
        print(f"{self.nome} saiu para uma caminhada por algumas horas!")

    def dormir(self):
        print(f"{self.nome} foi dormir!")
