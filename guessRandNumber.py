import random

print ('\n----Acerte o número!----')
vezes=0
random_num = random.randint(1, 1000)


while True:
    numero = int(input("Acerte o número sorteado: "))
    
    if numero == random_num:
        print ("Parabéns, número correto!")
        print (f"Foram necessárias {vezes} tentativas")
    elif numero >= random_num - 3 and numero <= random_num + 3:
        print ("Quase!")
    elif numero > random_num:
        print ("Tente um número menor!")
        vezes+=1
    else:
        print ("Tente um número maior!")
        vezes+=1





