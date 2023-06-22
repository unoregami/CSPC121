class Customer:
    greeting = "Welcome to Coffee Palace!\n===========================================================================================================\n"
    def __init__(self, name, beverage, food, total):
        self.name = name
        self.beverage = beverage
        self.food = food
        self.total = total

    def print(self):
        print(f"Name = {self.name}\t||\tBeverage = {self.beverage}\t||\tFood = {self.food}\t||\tTotal = {self.total}")

c_1 = Customer("Nate", "Espresso", "Pastrami on rye", 220)
c_2 = Customer("Elaine", "Strawberry frappuccino", "Tuna wrap", 270)
c_3 = Customer("Samirah", "Iced caffe latte", "Cinnamon roll", 230)
c_4 = Customer("Jerry", "Caramel macchiato", "Glazed doughnut", 230)
c_5 = Customer("Paz", "Iced tea", "Blueberry pancakes", 315)

print(Customer.greeting)
Customer.print(c_1)
Customer.print(c_2)
Customer.print(c_3)
Customer.print(c_4)
Customer.print(c_5)