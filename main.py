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

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}



def is_resources_sufficient(order_ingredients):
  """Return True when order can be made and False if it can't"""
  for item in order_ingredients:
    if order_ingredients[item] > resources[item]:
      print(f"Sorry not enough {item}")
      return False
  return True  
  
def process_coins():
  """Calculates the total coin value inserted"""
  print("Please insert your coins: ")
  total =  int(input("Quarters: ")) * 0.25
  total += int(input("Dimes: ")) * 0.10
  total += int(input("Nickles: ")) * 0.05
  total += int(input("Pennies: ")) * 0.01   
  return total

def is_transaction_successful(money_recieved, drink_cost):
  if money_recieved < drink_cost:
    print("Sorry that's not enough money. Money refunded.")
    return False
  else:
    global profit 
    profit += drink_cost
    change = round(money_recieved - drink_cost, 2)
    print(f"Here is ${change} dollars in change")
    return True
    

def make_coffee(drink_name, drink_resources):
  for item in drink_resources:
    resources[item] -= drink_resources[item]
  print(f"Enjoy your {drink_name}")
  
    
#TODO 1:  Prompt user by asking “What would you like?
is_on = True
while is_on:
  choice = input("What would u like? (espresso/latte/cappuccino): ").lower()
  if choice == "off":
    is_on = False
  #TODO 2: print report, it reports all the resources of the coffee machine  
  elif choice == "report":
    print(f"Water: {resources['water']} ml")
    print(f"Milk: {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']} g")
    print(f"Money: {profit}")
    
  # TODO 3: check if all resourses are sufficient and checks it agaisnt the recipes and updates  
  elif choice == "espresso" or "latte" or "cappuccino":
    drink = MENU[choice]
    if is_resources_sufficient(drink["ingredients"]):
      payment = process_coins()
      if is_transaction_successful(payment, drink["cost"]):
        make_coffee(choice, drink["ingredients"])
             
        
  else:
    print("Error")

    
  



