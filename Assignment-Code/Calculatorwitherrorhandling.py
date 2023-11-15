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
        try:
            return self.x / self.y
        except ZeroDivisionError:
            print("Error: Division by zero")
            pass


try:
    x = int(input("Enter your first number> "))
    y = int(input("Enter your second number> "))
    calculator = Calculator(x, y)
    z = calculator.divide()
    print(f"The division of {x} and {y} is {z}")
except ValueError:
    print("Error: Invalid input")