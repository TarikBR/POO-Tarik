num = input("Digite o dia da semana usando número (1-7): ")

try:
    data = int(num)
    if data == 1:
        print("O número informado é Domingo.")
    elif data == 2:
        print("O número informado é Segunda.")
    elif data == 3:
        print("O número informado é Terça.")
    elif data == 4:
        print("O número informado é Quarta.")
    elif data == 5:
        print("O número informado é Quinta.")
    elif data == 6:
        print("O número informado é Sexta.")
    elif data == 7:
        print("O número informado é Sábado.")
    else:
        print("Valor inválido!")
except:
    print("Valor inválido!")
