from calculation import Add, Subtract, Multiply, Divide 

class CalculationFactory:
    def calculation(self, operation):
        if operation == "add":
            return Add()
        elif operation == "subtract":
            return Subtract()
        elif operation == "multiply":
            return Multiply()
        elif operation == "divide":
            return Divide() 
        else:
            return ValueError("Invalid operation type") 