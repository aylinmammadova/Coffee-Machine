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

profit = 0


def is_resource_sufficient(order_ingredients):
    """Return True if there is enough resources, or False if not."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
        else:
            return True


def process_coins():
    """Return total amount of inserted coins."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True if payment is accepted, False if insufficient."""
    if drink_cost > money_received:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif drink_cost <= money_received:
        change = round(money_received - drink_cost, 2)
        global profit
        profit = round(profit + change, 1)
        print(f"Here is ${change} dollars in change.")
        return True


def make_coffee(order_ingredients, drink_name):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] = resources[item] - order_ingredients[item]
    print(f"Here is your {drink_name}. Enjoy!")


is_on = True

while is_on:
    # Prompt user by asking “ What would you like? (espresso/latte/cappuccino): "
    choice = input(" What would you like? (espresso/latte/cappuccino): ").lower()
    # TODO: 2. Turn off the Coffee Machine by entering “ off ” to the prompt.
    if choice == "off":
        is_on = False
    # Print report.
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        # Check resources sufficient?
        if is_resource_sufficient(drink["ingredients"]):
            # Process coins.
            payment = process_coins()
            # Check transaction successful?
            if is_transaction_successful(payment, drink["cost"]):
                # Make Coffee.
                make_coffee(drink["ingredients"], choice)
                
                