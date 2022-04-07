
# 1st Step done !
books = input("Enter the name of books : ")
price = int(input("Enter the price of book : "))
publisher = input("Enter the name of publisher : ")

# 2nd Step store it in text  file
file2write=open("Book Database",'w')
file2write.write(books)
file2write.close()

# 3rd Step 
answer = input("Do you want to display books y/n")

# 4th Step
if(answer == "n"):
        print("Thank you for visiting ! :)")
else:
        f=open("Book Database",'r')
        Listofbooks = f.read()
        print(Listofbooks)

