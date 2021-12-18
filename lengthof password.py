import random
passlen = int(input("Enter the password length\n"))
s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%&^()?"
p = "".join(random.sample(s,passlen))
print(p)
