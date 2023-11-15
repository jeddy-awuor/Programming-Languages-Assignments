
#JEDDY AWUOR ODUOR, SCT211-0027/20022

#print("Calculator Assignment")
#x = int(input("Enter your first number> "))
#y = int(input("Enter your second number> "))
#z = x + y
#print(f"The sum of {x} and  {y} is {z}") #add the 'f' in front



print("Calculator Assignment2")
class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self):
        return self.x + self.y

    def subtract(self):
        return self.x - self.y

    def multiply(self):
        return self.x * self.y

    def divide(self):
        return self.x / self.y

x = int(input("Enter your first number> "))
y = int(input("Enter your second number> "))
calculator = Calculator(x, y)
z = calculator.add()
print(f"The sum of {x} and {y} is {z}")


