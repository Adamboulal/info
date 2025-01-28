import random as r


massimo=int(input("dammi il massimo di tentativi: "))

def genera_numero(n1):
    n1=r.randint(0, massimo)
    return n1


n1=genera_numero(massimo)
tentativi=massimo//10
if massimo<10:
    tentativi=1

print(f"i tuoi tentativi sono: {tentativi}")

for i in range(tentativi):
    n2=int(input("dammi un numero: "))

    if n2==n1:
        print("congratulazioni, hai vinto!")
        quit(0)
    elif n2<n1:
        print("il numero è troppo piccolo")
    else:
        print("il numero è troppo grande")
