#Problema 1: trovare i divisori di un numero
def divisori_numero(numero:int) :

    divisori = []
    for i in range (1 , numero + 1):
        
        if numero % i == 0:
            divisori.append(i)

    return divisori

#Problema 2: verificare se un numero è primo
def numero_primo(numero: int):
    divisori = divisori_numero(numero)
    if len(divisori) == 2 :
        return True
    else :
        return False


#Problema 3: trovare tutti i numeri primi più piccoli di un certo valore

def numeri_primi(numero: int):
    primi = [2]
    for i in range (3, numero + 1, 2):
        primo = numero_primo(i)
        if primo == True :
            primi.append(i)
    return primi


#Problema 4: stabilire se due numeri sono coprimi

def numeri_coprimi(numero1: int, numero2: int) -> bool:
    coprimi = True
    for i in range(2, min(numero1, numero2) + 1):
        if numero1 % i == 0 and numero2 % i == 0:
            coprimi = False 
            break
    return coprimi
    
#Problema 5: Calcolare la funzione di Eulero

def eulero(numero: int):
    eulero = 0
    for i in range (1 , numero):
        if numeri_coprimi(i, numero):
            eulero += 1
    return eulero
print(eulero(15))

