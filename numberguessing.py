import time

print('you have to guess the number from the given  list below')

guess_number= '1','3','5','4','6','2'
time.sleep(0.7)
print(guess_number)

while True:
    ans = input (int('>>'))

    if ans in  guess_number:
        print("yes It is right number. you won")
    else:
        print("No it is not a right number. Try Again")
        break
