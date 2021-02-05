
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


keep_buying = True
money = 0


def investigate_resources(drink):
    ingredients = drink["ingredients"]
    for key in ingredients:
        if ingredients[key] > resources[key]:
            print(f"Sorry, there is not enough {key}")
            return False
    return True


def proceed_with_request(drink, quarters, dimes, nickels, pennies):
    global money
    """If the resources are sufficient and the amount of money is greater than
    the cost of the drink, proceed with payment."""
    money += MENU[drink]["cost"]
    change = amount_entered(quarters, dimes, nickels, pennies) - MENU[drink]["cost"]
    print(change)
    ingredients = MENU[drink]["ingredients"]
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]
    if change > 0:
        print(f"Here is ${round(change, 2)} in change.")
    print(f"Here is your {drink} ☕. Enjoy!")


def amount_entered(quarters, dimes, nickels, pennies):
    return round(quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01, 2)


def report(res):
    print("Water: ", res["water"], "ml")
    print("Milk: ", res["milk"], "ml")
    print("Coffee: ", res["coffee"], "g")
    print("Money $", money)


while True:
    drink_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if drink_choice == "report":
        report(resources)
    elif drink_choice == "off":
        break
    else:
        drink = MENU[drink_choice]
        quarters = int(input("how many quarters? "))
        dimes = int(input("How many dimes? "))
        nickels = int(input("How many nickels? "))
        pennies = int(input("How many pennies? "))
        amount_paid = amount_entered(quarters, dimes, nickels, pennies)
        if amount_paid < drink["cost"]:
            print("Sorry that's not enough money. Money refunded.")
        else:
            enough_resources = investigate_resources(drink)
            if enough_resources:
                proceed_with_request(drink_choice, quarters, dimes, nickels, pennies)
