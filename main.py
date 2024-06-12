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
            if check_recourses(choice):
                payment = process_coins()
                if check_transaction_successful(payment, MENU[choice]["cost"]):
                    make_coffee(choice)
        else:
            print("Invalid input. Please choose from espresso, latte, or cappuccino. To exit type 'off'. To check "
                  "resources, type 'resources'")


def make_coffee(drink):
    for item in MENU[drink]["ingredients"]:
        resources[item] -= MENU[drink]["ingredients"][item]
    resources["money"] += MENU[drink]["cost"]
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


def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickels = int(input("How many nickels? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    return quarters + dimes + nickels + pennies


def check_transaction_successful(payment, drink_cost):
    if payment >= drink_cost:
        change = round(payment - drink_cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


if __name__ == "__main__":
    user_prompt()
