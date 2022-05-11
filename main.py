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
    "money": 2.5
}

user_choice = input("What would you like? (espresso/latte/cappuccino): ")


def end_choice(choice):
    if choice == "off":
        return


end_choice(user_choice)


def report_choice(res,choice):
    if choice == "report":
        print(f"Water : {res['water']}")
        print(f"Milk : {res['milk']}")
        print(f"Coffee : {res['coffee']}")
        print(f"Money : ${res['money']}")
    else:
        return


report_choice(resources,user_choice)