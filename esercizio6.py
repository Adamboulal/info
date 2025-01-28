scelta=input("scegli tra : area del quadrato (1) o area cerchio (2): ")
if scelta == "1":
    n=int(input("dammi il lato del quadrato: "))
    area=n*n
    print(area)
elif scelta== "2":
    n1=int(input("dammi il raggio del cerchio"))
    area=3.14*n1
    print(area)
else:
    print("errore")