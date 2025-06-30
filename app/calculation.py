import math 

class Add:
    def add(x, y):
        return x + y

class Subtract:
    def subtract(x, y):
        return x - y 

class Multiply:
    def multiply(x, y):
        return x * y 

class Divide:
    def divide(x, y):
        return x / y 

class Root:
    def root(x, y):
        return math.pow(x, 1 / y) 

class Power:
    def power(x, y):
        return math.pow(x, y)

class Modulus:
    def remainder(x, y):
        return x % y 

class Percentage:
    def percentage(x, y):
        return (x / y) * 100

class AbsoluteDiff:
    def absolute_diff(x, y):
        return abs(x - y)