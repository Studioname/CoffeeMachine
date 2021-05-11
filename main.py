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

coins = {
    "quarter" : 0.25, 
    "dime" : 0.10, 
    "nickel" : 0.05, 
    "cent" : 0.01
    }


hopper = 0


def report():
    for ingredient in resources:
        print(f"{ingredient} : {resources[ingredient]} remaining")
    global hopper
    print(f"Hopper contains: ${hopper}")

# Coffee Machine Program Requirements
# 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
def choose_drink():
    choose_drink = input("What drink would you like? (espresso/latte/cappuccino)\n")
    if choose_drink == "off":
        quit()
    elif choose_drink == "report":
        report()

    return choose_drink

# a. Check the user’s input to decide what to do next.
def check_ingredients(choice):
    for ingredient in MENU[choice]["ingredients"]:
        sufficient_ingredients = True
        if MENU[choice]["ingredients"][ingredient] > resources[ingredient]:
            sufficient_ingredients = False
            print(f"Sorry! Not enough {ingredient} to make a {choice}")
            return sufficient_ingredients
        return True


def dispense_cup():
    print("Cup dispensed.")


def remove_ingredients(choice):
    for ingredient in MENU[choice]["ingredients"]:
        resources[ingredient] -= MENU[choice]["ingredients"][ingredient]
    dispense_cup()
    print("Ingredients being turned into coffee")


def insert_coins(drink):
    print(f"Please insert ${MENU[drink]['cost']} in coins." )
    sum = 0
    for coin in coins:
        coins_added = input(f"How many {coin}s would you like to add?\n")
        while coins_added.isnumeric() == False:
            coins_added = input(f"How many {coin}s would you like to add?\n")
        coins_added = int(coins_added)
        to_add = coins_added * coins[coin]
        global hopper
        hopper += to_add
        sum += to_add
    if sum > MENU[drink]['cost']:
        change = sum - MENU[drink]['cost']
        print(f"Too much given. Returning {round(change, 2)} in change")
        hopper -= change
        sum = 0
        return True
    elif sum < MENU[drink]['cost']:
        print(f"Not enough given. Returning coins.")
        hopper -= sum
        sum = 0
        return False
    else:
        print("Correct change given. Thank you for your order!")
        return True


def serve_drink(drink):
    print(f"Here is your {drink}! Enjoy")


def coffee_machine():
    choice = choose_drink()
    if choice in MENU:
        if check_ingredients(choice) == True:
            if insert_coins(choice):
                remove_ingredients(choice)
                serve_drink(choice)
                coffee_machine()
            else:
                coffee_machine()
        else:
            coffee_machine()
                    
    else:
        coffee_machine()


coffee_machine()


# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.
# 2. Turn off the Coffee Machine by entering “off” to the prompt.
# a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
# the machine. Your code should end execution when this happens.
# 3. Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.
# 5. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
# 6. Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected.
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say “Sorry that's not enough money. Money refunded.”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
# places.
# 7. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
# latte was their choice of drink