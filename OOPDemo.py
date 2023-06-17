class Calculator:
    num = 100  # class variable

    # default constructor
    def __init__(self, a, b):
        self.first_num = a
        self.second_num = b
        print("I am called automatically when object is created.")

    def getData(self):
        print("I am now executing as method in class")

    def addition(self):
        return self.first_num + self.second_num + self.num


obj = Calculator(2, 7)  # syntax to create objects in python

obj.getData()
print(obj.addition())

obj2 = Calculator(10, 90)  # syntax to create objects in python

obj2.getData()
print(obj2.addition())
