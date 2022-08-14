"""
Object-Oriented Programming and classes
Uses classes and methods (function part of a class is called a method)

Methods created in the same class all share the same characteristics

Everything in Python is an object

Ctrl-click on the __add__ method to get details
Note the + and __add__ go to the same built-in

Class: template for creating objects. All objects created using
the same class will have the same characteristics

Object: An instance of a class

Instantiate: Create an instance of a class

Method: A function defined in a class

Attribute: A variable bound to an instance of a class

self: Reference to an instance of the class
"""
a = 12
b = 4
print(a + b)  # 16
print(a.__add__(b))  # 16


class Kettle(object):

    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        self.on = True


kenwood = Kettle("Kenwood", 8.99)
print(kenwood.make)
print(kenwood.price)

kenwood.price = 12.75
print(kenwood.price)

hamilton = Kettle("Hamilton", 14.55)

print("Models: {} = {}, {} = {}".format(kenwood.make, kenwood.price, hamilton.make, hamilton.price))

# Because kenwood and hamilton are objects, we can use them in replacement fields
print("Models: {0.make} = {0.price}, {1.make} = {1.price}".format(kenwood, hamilton))

print(hamilton.on)
hamilton.switch_on()
print(hamilton.on)

Kettle.switch_on(kenwood)
print(kenwood.on)

print("*" * 80)

kenwood.power = 1.5
print(kenwood.power)

# All three of the power_source attribute as it was defined in the class
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)
print(Kettle.__dict__)
print(kenwood.__dict__)
print(hamilton.__dict__)

print("Switch to atomic power")
Kettle.power_source = "atomic"
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)

print("Switch kenwood to gas")
kenwood.power_source = "gas"
print(Kettle.power_source)
print(kenwood.power_source)
print(hamilton.power_source)





