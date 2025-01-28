import random 
def roll(sides: int = 6) -> int:
        return random.randint(1, sides)
hp=100
turni=0
while hp > 0:
    turni += 1
    danno=roll(sides=6)
    hp=hp - danno
    if hp < 0:
          hp = 0
    print(f"la tua vita è {hp}")
    print(f"hai subito {danno} danni!")

print(f"il gioco è terminato hai giocato{turni}")