from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

machine_on = True
while machine_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ").lower()
    if choice == "off":
        machine_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
         drink = menu.find_drink(choice)
         drink_cost = drink.cost
         if coffee_maker.is_resource_sufficient(drink=drink):
             if money_machine.make_payment(drink_cost):
                coffee_maker.make_coffee(drink)






