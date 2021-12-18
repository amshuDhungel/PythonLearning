import random

while True:
    print('''1.roll the dice\n      2.exit\n''')
    num = int(input("Enter your dice number: "))
    if num == 1:
        num = random.randint(1, 6)
        print(num)
    else:
        break