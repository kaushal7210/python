print("Welcome to the coffee maker.")
MENU = {
        "espresso": {
            "ingredients": {
                "coffee": 18,
                "water": 50,
            },
            "cost": 10,

        },
        "latte": {
            "ingredients": {
                "coffee": 18,
                "water": 50,
                "milk": 24,
            },
            "cost": 20,
        },
        "cappuccino": {
            "ingredients": {
                "coffee": 24,
                "water": 250,
                "milk": 100,
            },
            "cost": 30,
        }
    }

resources = {
    "coffee": 2000,
    "water": 20000,
    "milk": 10000,
}


def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    print("please insert coins")
    total = int(input("how many coins?:"))
    return total


def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"here is Rs{change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("sorry that's mot enough money.money refunded.")
    return False


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕. Enjoy!")


profit = 0
is_on = True
while is_on:
    choice = input("What do you want?(latte/espresso/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water:{resources['water']}ml")
        print(f"coffee:{resources['coffee']}gm")
        print(f"milk:{resources['milk']}ml")
        print(f"money:Rs{profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
