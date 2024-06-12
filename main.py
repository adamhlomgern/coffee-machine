# Global Variables
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

MENU = {
    "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
    "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
    "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0},
}


# My functions

def user_prompt():
    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice == "report":
            report()
        elif choice == "off":
            off()
        elif choice in MENU:



def make_coffee(drink):
    for item in MENU[drink]["ingredients"]:
        resources[item] -= MENU[drink]["ingredients"][item]
    print(f"Here is your {drink}. Enjoy!")


def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def off():
    print("Turning off the machine. Goodbye!")
    exit()


def check_recourses(drink):
    for item in MENU[drink]["ingredients"]:
        if MENU[drink]["ingredients"][item] > resources[item]:
            print(f"There is not enough {item}.")
            return False
    return True