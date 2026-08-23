def taking_order():
    print('Hello ! Welcome to Network Chuck coffe shop ' )
    name=input('What is your name ?')
    print ('Hello' , name ,'Wht would you like to order .Pls take a look at the menu ')
    menu ='Espresso (Cost :Rs .70 ) , Latte (Cost: Rs .70 )\n'
    print(menu)
    order=input('Pls input your choice\n')
    print (name,'your',order,' is being placed\n')

    x=order.lower()
    if 'espresso' in x and 'latte' in x:
        espresso_qty=int(input('How many espresso would you like to order?\n'))
        latte_qty=int(input('How many latte would you like to order?\n'))
        total_cost=(70*(espresso_qty+latte_qty))
    elif 'espresso' in x:
        quantity_espresso=int(input('How many espresso would you like to order?\n'))
        total_cost=70 * quantity_espresso
    elif 'latte' in x:
        quantity_latte=int(input('How many latte would you like to order?\n'))
        total_cost=70*quantity_latte
    else:
        print('Sorry we could not find your order in our menu')
        return 
    print('Your total cost is: Rs.',total_cost)
    check=input('Would you like to order again? \n')
    if (check.lower()=='yes'):
        taking_order()
    else:
         print('Thank you are choosing Network Chuck coffe shop.Have a nice day')
    print('please visit us again')
taking_order()

