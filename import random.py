import random 

opcoes = ["pedra", "papel", "tesoura"]

computador = random.choice(opcoes)

jogador = input("escolha pedra ou papel ou tesoura") .lower()

print ("computador escolheu: "< computador)

if jogador == computador: 
    print ("empate")

    if jogador == "pedra":
        if computador == "tesoura":
        print ("voce venceu!!")
    else: 
        print("voce perdeu!!")

if jogador == "papel":
        if computador == "pedra":
        print ("voce venceu!!")
    else: 
        print("voce perdeu!!")

        if jogador == "pedra":
        if computador == "tesoura":
        print ("voce venceu!!")
    else: 
        print("voce perdeu!!")




