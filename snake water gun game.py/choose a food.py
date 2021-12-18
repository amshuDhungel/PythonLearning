menu = {}
menu['1']= "Mo: Mo(chicken, veg, buff)                   Rs.100"
menu['2']= "chowmin veg                                  Rs.040"
menu['3']= "chicken chowmin, ramen noodles               Rs.120"
menu['4']= "small pizza(mixed, tomatoes, cheese)         Rs.300"
menu['5']= "french fries per plate                       Rs.250"

while True:
    option = menu.keys()
    option.sort()
    for entry in option:
        print(entry[menu])
    customer = input("please select a food", menu)
    
    
    if customer == '1':
        print("Your order is " + menu['1'])
    if customer == '2':
        print("Your order is " + menu['2'])
    if customer == '3':
        print("Your order is " + menu['3'])
    if customer == '4':
        print("Your order is " + menu['4'])
    if customer == '5':
        print("Your order is " + menu['6'])
    if customer == '0':
        break
    else:
        print("options are not available. please select from above menu")
