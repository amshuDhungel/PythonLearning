# name : Mr. A. D.Luffy
#description: text based adventure  game

import time



print("KNOCK! KNOCK! KNOCK!")
print("yes")
time.sleep(0.2)
print("""A man of 40 years came to my house. He said to me that
his car get punctured. It was at night 9pm in a rainy road. He asked me to provide him a shelter""")
time.sleep (0.2)
print(" Will you provide shelter to him")

Ans_yes= "Yes", "y","Y" 
Ans_no= "No","n" ,"N"
time.sleep(0.2)

ans1 = input(">>")

if ans1 in Ans_yes:
    print("Police arrived and asked whether thief is inside")
    
    ans2 = input(">>")

    if ans2 in Ans_yes:
        print("The police said thank you and reward  me 2000$ for my bravery to catch theif. YOU WIN!!")

    elif ans2 in Ans_no:
        print("You helped the theif. The theif attack and kill you. YOU LOSE")

    else:
        print("This is not valid")
    
elif ans1 in Ans_no:
    print ("The theif is trying to kill you. There is hammer nearby")
    ans3 = input(">>")

    if ans3 in Ans_yes:
        print("You grab a hammer and knock  him down. Congratulation You win.")

    elif ans3 in Ans_no:
        print("He killed you. You Lose.")

    else:
        print("This is  not valid")



