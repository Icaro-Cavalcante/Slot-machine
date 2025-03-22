print ("Seja bem-vindo ao jogo de Slot Machine 🐱")
print ("-------------------------------------------")
print ("Para ganhar, você precisa girar a roleta e conseguir 3 símbolos iguais.")
print ("Lembrando que você só precisa de sorte.")
print ("-------------------------------------------")
print ("A cada rodada você aposta uma quantia em dinheiro.")
print ("Caso ganhe, você recebe 10 vezes o valor da aposta.")
print ("Caso perca, você perde o dinheiro que apostou.")
print ("-------------------------------------------")

import random
import time
slot = ["🍥", "🐲", "🐯", "🦄", "💀"]
active = True
sae = []
money = 0
dinheiro = float(input("Quanto de dinheiro você tem? R$"))
money += float(dinheiro)

while active:
    champagne = float(input("Qual o valor da sua aposta? R$"))
    while champagne > money:
       print ("-------------------------------------------")
       print ("Você não pode apostar mais do que tem. Tente novamente.")
       champagne = float(input("Qual o valor da sua aposta? R$"))

    def victory():
      print ("Você ganhou, parabéns!")
      print ("-------------------------------------------")
    def defeat():
     print ("Você perdeu.")
     print ("-------------------------------------------")

    sae = []
    random.shuffle(slot)
    sae.append(slot[0])
    random.shuffle(slot)
    sae.append(slot[1])
    random.shuffle(slot)
    sae.append(slot[2])

    print ("-------------------------------------------")
    print("So we roll the dice")
    time.sleep(1)
    print("See where they may fall~")
    print ("")
    time.sleep(1)
    roll = (sae[0], sae[1], sae[2])
    horário = 3
    for gay in range (horário, 0, -1):
        print (gay)
        time.sleep (1)
    print ("-------------------------------------------")
    print (roll)
    if roll == ('🍥', '🍥', '🍥'):
        victory ()
        money+= champagne * 10
    elif roll == ('🐲', '🐲', '🐲'):
        victory ()
        money+= champagne * 10
    elif roll == ('🐯', '🐯', '🐯'):
        victory ()
        money+= champagne * 10
    elif roll == ('🦄', '🦄', '🦄'):
        victory ()
        money+= champagne * 10
    elif roll == ('💀', '💀', '💀'):
        victory ()
        money+= champagne * 10
    else:
        defeat ()
        money-= champagne

    print (f"Você tem agora R${money}")
    if money <= 0:
       print ("Sem dinheiro suficiente para outra rodada.")
       break

    nijima = input ("Deseja jogar novamente? (S/N) ")
    if nijima.upper() == "S":
       print ("-------------------------------------------")
       print ("Vamos jogar mais uma vez 🐱")
    while nijima.upper() != "S" and nijima.upper() != "N":
       print ("-------------------------------------------")
       print ("Digite uma opção válida.")
       nijima = input ("Deseja jogar novamente? (S/N) ")
    if nijima.upper() == "N":
        kiryu = False

print ("-------------------------------------------")
print ("Obrigado por ter jogado.")
       
       
       

