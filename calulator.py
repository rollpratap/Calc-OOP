# %%

class calculator():
    def __init__(self, x, y):
        self.x = x 
        self.y = y

    def add(self):
        print("Sum :", self.x + self.y)

    def subtraction(self):
        print("Subtraction :", self.x-self.y)

    def multiplication(self):
        print("Multiplication:", self.x*self.y)

    def division(self):
        print("Division:", self.x/self.y)


x = int(input("Enter X:"))
y = int(input("Enter y:"))

n1 = calculator(x,y)


choice = 1 
while choice != 0:
    print("1. ADD")
    print("2. SUB")
    print("3. Multiplication")
    print("4. Division")

    choice = int(input("Enter your choice:"))

    if choice == 1:
        print(n1.add())
    elif choice == 2:
        print(n1.subtraction())
    elif choice == 3:
        print(n1.multiplication())
    elif choice == 4:
        print(n1.division())
    else:
        print("Invalid choice")

# n1.add()
# n1.subtraction()
# n1.multiplication()
# n1.division()


# %%



