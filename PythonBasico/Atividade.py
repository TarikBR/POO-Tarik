precos = []
for i in range(3):
    precos.append(float(input("Digite um preço: ")))

if precos[0] < precos[1] and precos[0] < precos[2]:
    print(f"O primeiro produto de preço {precos[0]} é o mais barato!")
elif precos[1] < precos[0] and precos[1] < precos[2]:
    print(f"O segundo produto de preço {precos[1]} é o mais barato!")
else:
    print(f"O terceiro produto de preço {precos[2]} é o mais barato!")
