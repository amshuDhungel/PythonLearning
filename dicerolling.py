import random
while True:
    print('Do you want to roll a dice') 
    print('1.Roll a dice\n   2.exit\n')
    answer = int(input("Enter your number: "))

    if  answer == 1:
        answer=random.randint(1, 6)
        print(answer)
    else:
        break

        
