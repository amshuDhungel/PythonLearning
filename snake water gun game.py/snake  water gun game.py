import random

def gameWin(comp, b):
    if comp == 's':
        if  b == 'w':
            return False
        elif b== 'g':
            return True
    elif comp == 'w':
        if  b == 'g':
            return False
        elif b== 's':
            return True
    elif comp == 'g':
        if  b == 's':
            return False
        elif b== 'w':
            return True
        

print("Comp Turn: Snake(s) Water(w) or Gun(g)?")
randNo = random.randint(1, 3)
print(randNo)
if randNo ==1:
    comp = 's'
elif randNo == 2:
    comp = 'w'
elif randNo == 3:
    comp = 'g'

b = input("Player's Turn: Snake(s) Water(w) or Gun(g)? ")
a = gameWin(comp ,b)

print(f"Computer chose {comp}")
print(f"Computer chose{b}")

if a == None:
    print("The game is a tie ")
elif a:
    print("You win!")
else:
    print("You Lose!")
