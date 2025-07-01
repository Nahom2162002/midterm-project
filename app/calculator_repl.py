from operations import CalculationFactory as o  
from history import History as h 
from calculator_memento import Caretaker as c 

def main():
    history_file = open("history.txt", "w+")
    while True:
        try:
            print("Would you like to add, subtract, multiply, divide, root, power, modulus, percentage, absolute?")
            user_input = input(">>> ")
            
            if user_input.lower() in ("exit()", "quit()"):
                history_file.close() 
                break 

            if user_input.lower() in ("help"):
                print("This advanced calculator allows you to perform 4 operations of your choice:" \
                "add: Adds two values of your choice" \
                "subtract: Subtracts two values of your choice" \
                "multiply: Multiplies two values of your choice" \
                "divide: Divides two values of your choice" \
                "root: Returns the square root of a value of your choice" \
                "Example: '>>> add" \
                "'Input two numbers to add: '" \
                ">>> 2" \
                ">>> 3" \
                "2 + 3 = 5")
            
            if user_input.lower() in ("history"):
                h.help(history_file)
            
            if user_input.lower() in ("undo"):
                c.undo() 
            
            if user_input.lower() in ("redo"):
                c.redo() 

            result = eval(user_input)
            
            if result is not None:
                match user_input:
                    case "add":
                        print("Input two numbers to add: ")
                        try:
                            x = int(input())
                            y = int(input())
                            calculation = o.calculate("add")
                            print(x, "+", y, "=", calculation.add(x, y))
                            history_file.write(str(x), "+", str(y), "=", str(calculation.add(x, y)))
                        except ValueError:
                            print("ERROR: Please input an integer only")
                    case "subtract":
                        print("Input two numbers to subtract: ")
                        try:
                            x = int(input())
                            y = int(input())
                            calculation = o.calculate("subtract")
                            print(x, "+", y, "=", calculation.subtract(x, y))
                            history_file.write(str(x), "+", str(y), "=", str(calculation.subtract(x, y)))
                        except ValueError:
                            print("ERROR: Please input an integer only")
                    case "multiply":
                        print("Input two numbers to multiply")
                        try:
                            x = int(input())
                            y = int(input())
                            calculation = o.calculate("multiply")
                            print(x, "+", y, "=", calculation.multiply(x, y))
                            history_file.write(str(x), "+", str(y), "=", str(calculation.multiply(x, y)))
                        except ValueError:
                            print("ERROR: Please input an integer only")
                    case "divide":
                        print("Input two numbers to divide")
                        try:
                            x = int(input())
                            y = int(input())
                            calculation = o.calculate("divide")
                            print(x, "+", y, "=", calculation.divide(x, y))
                            history_file.write(str(x), "+", str(y), "=", str(calculation.divide(x, y)))
                        except ValueError:
                            print("ERROR: Please input an integer only")
                        except ZeroDivisionError:
                            print("ERROR: Can't divide by zero!")
                    case "root":
                        print("Input a number and the nth root")
                        try:
                            x = int(input())
                            y = int(input())
                            calculation = o.calculate("root")
                            print(y, "th root of", x, ":", calculation.root(x, y))
                            history_file.write(y, "th root of ", str(x), ":", str(calculation.root(x, y)))
                        except ValueError:
                            print("ERROR: Please input an integer only")
                    case "power":
                        print("Input a number and the power")
                        try:
                            x = int(input())
                            y = int(input())
                            calculation = o.calculate("power")
                            print(x, "to the", y, "th power = ", calculation.power(x, y))
                            history_file.write(x, "to the", y, "th power = ", str(calculation.power(x, y)))
                        except ValueError:
                            print("ERROR: Please input an integer only")
                    case "modulus":
                        print("Input two values")
                        try:
                            x = int(input())
                            y = int(input())
                            calculation = o.calculate("modulus")
                            print("Remainder of ", x, "and", y, "=", calculation.remainder(x, y))
                        except ValueError:
                            print("ERROR: Please input integers only")
                    case "percentage":
                        print("Input two values")
                        try:
                            x = int(input())
                            y = int(input())
                            calculation = o.calculate("percentage")
                            print(x, "% of", y, "=", calculation.percentage(x, y))
                        except ValueError:
                            print("ERROR: Please input integers only")
                    case "absolute":
                        print("Input two values")
                        try:
                            x = int(input())
                            y = int(input())
                            calculation = o.calculate("absolute")
                            print("Absolute difference of", x, "and", y, "=", calculation.absolute_diff(x, y))
                        except ValueError:
                            print("ERROR: Please input integers only")
        
        except Exception as e:
            print(f"Error: {e}")

if __name__ == '__main__':
    main()