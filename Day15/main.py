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
    "coffee": 100
}

profit = 0.0


def check_resources(drink_choice):
    ingredients = MENU[drink_choice]['ingredients']
    results = []
    for ingredient in ingredients:
        has = resources[ingredient]
        needs = ingredients[ingredient]
        if needs > has:
            results.append(False)
            print(f"Sorry there's not enough {ingredient}")
        else:
            results.append(True)

        if False in results:
            return False
        else:
            return True


def update_resources(drink_choice):
    ingredients = MENU[drink_choice]['ingredients']
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]


def print_report():
    print(f"Water:  {resources['water']}ml")
    print(f"Milk:  {resources['milk']}ml")
    print(f"Coffee:  {resources['coffee']}g")
    print(f"Money:  ${profit}")


def add_change(q, d, n, p):
    return (q * .25) + (d * .10) + (n * .05) + (p * .01)


off = False

while not off:
    choice = input("What would you like? (espresso/latte/cappuccino):")

    if choice == "off":
        off = True
    elif choice == "report":
        print_report()
    else:
        choice_available = check_resources(choice)
        if choice_available:
            drink_price = MENU[choice]["cost"]
            quarters = int(input("How many quarters are you using? "))
            dimes = int(input("How many dimes are you using? "))
            nickels = int(input("How many nickels are you using? "))
            pennies = int(input("How many pennies are you using? "))
            money_given = add_change(quarters, dimes,nickels, pennies)
            if money_given == drink_price:
                profit += money_given
                update_resources(choice)
            elif money_given > drink_price:
                update_resources(choice)
                print(f"Here is ${money_given - drink_price} in change")
                profit += drink_price
            else:
                print(f"Sorry {choice} cost {drink_price}, that was only {money_given}")

        else:
            print("Not enough resources, please try a different selection.")

