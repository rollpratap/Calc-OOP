# %%

class calculator(): 
# Convention dictates that the first letter of your class be capital with subsequent words in camel case
# So you can rename this to Calculator. Also the () brackets are unnecessary unless you are inheriting(another OOP concept) from some other class
# Camel case means you start with a upper case letter for every new word. For eg. class ThisIsMyClassInCamelCase:
    def __init__(self, x, y):
	# How useful is this? In the sense, for every new calculation you will have to create a new instance of your calculator
	# Analogous to buying a new calculator everytime you want to calculate something new. Not practical, is it?
        self.x = x 
        self.y = y

    def add(self):
	# Print is good. Returning is better.
	# i.e. return self.x + self.y
	# Also, how about accepting arguments in the method?
	# These comments are valid for all methods below
        print("Sum :", self.x + self.y)

    def subtraction(self):
        print("Subtraction :", self.x-self.y)

    def multiplication(self):
        print("Multiplication:", self.x*self.y)

    def division(self):
        print("Division:", self.x/self.y)

# Nice. Accepting user input
x = int(input("Enter X:"))
y = int(input("Enter y:"))

n1 = calculator(x,y)

# Nice implementation of the menu. But what if the user wants to calculate on different numbers everytime until they exit? Think over this...
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

"""
Nifty and widely used trick in python
Instead of putting executable code directly in the module(for example the while loop you have used above)
python allows you to wrap this code up in an if statement that executes only when the file is called. I will
explain the reasons why this is done in a call. Anyway, the trick is as follows

if __name__ == "__main__":
	
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


This is considered a good coding practice. It often filters out ultra newbs in coding interviews ;)
"""

# %%



