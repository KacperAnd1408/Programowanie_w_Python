

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}



def checking_water(chosen_drink):
    if resources['water'] >= MENU[chosen_drink]['ingredients']['water']:
        return True
    else:
        print("Sorry, there is no enough water.")
        return False

def checking_milk(chosen_drink):
    if chosen_drink != 'espresso':
        if resources['milk'] >= MENU[chosen_drink]['ingredients']['milk']:
            return True
        else:
            print("Sorry, there is no enough milk.")
            return False
    else:
        return True

def checking_coffee(chosen_drink):
    if resources['coffee'] >= MENU[chosen_drink]['ingredients']['coffee']:
        return True
    else:
        print("Sorry, there is no enough coffee.")
        return False

def processing_coins():
    penny = int(input("How many pennies do you have?: ")) * 0.01
    nickle = int(input("How many nickles do you have?: ")) * 0.05
    dime = int(input("How many dimes do you have?: ")) * 0.1
    quarter = int(input("How many quarters do you have?: ")) * 0.25
    total_insert = penny + nickle + dime + quarter
    return total_insert

def is_transaction_successful(chosen_drink, insert):
    global profit
    total_price = MENU[chosen_drink]['cost']
    if total_price > insert:
        return False
    elif total_price == insert:
        profit += total_price
        return True
    else:
        #change = 0
        change = insert - MENU[chosen_drink]['cost']
        change = round(change, 2)
        print(f"Here's ${change} in change.")
        profit += total_price
        return True

def deducting_resources(chosen_drink):
    resources["water"] -= MENU[chosen_drink]['ingredients']['water']
    if chosen_drink != 'espresso':
        resources["milk"] -= MENU[chosen_drink]['ingredients']['milk']
    resources["coffee"] -= MENU[chosen_drink]['ingredients']['coffee']



#penny = 1 cent, nickel = 5 cents, dime = 10 cents, quarter = 25cents
#print report - what resources has left
#check if the resources are sufficient to do sth - if not - print sorry, there is no {milk} enough.
#process coins - please insert coins...
#check transaction is successful - if not print not enough money - if yes odlicz zasoby i zycz milej kawy

is_working = True

profit = 0



def coffee_machine():
    global profit
    is_working_machine = True
    # resources['Money $'] = profit

    while is_working_machine:
        decision1 = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if decision1 == 'off':
            is_working_machine = False
        elif decision1 == 'report':
            for key, value in resources.items(): #!!!!!!!!!!!!!!!!!!!!!!!!!!
                print(f" {key}: {value}")
            print(f" Money: ${profit}")
        else:
            #global drink
            for drink in MENU:

                if drink == decision1:

                    is_enough_water = checking_water(drink)
                    is_enough_milk = checking_milk(drink)
                    is_enough_coffee = checking_coffee(drink)

                    if is_enough_water == True and is_enough_milk == True and is_enough_coffee == True:
                        #processing_coins()
                        check_coins = is_transaction_successful(chosen_drink=drink, insert=processing_coins())
                        if check_coins:
                            deducting_resources(drink)
                            print(f"Here is your {drink}. Enjoy!")
                            coffee_machine()
                        else:
                            print("Sorry that's not enough money. Money refunded.")
                            coffee_machine()

                    else:
                        is_working_machine = False


coffee_machine()