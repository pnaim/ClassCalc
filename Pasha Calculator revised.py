class Calculator:
    def __init(self, number1, number2):
        self.number1 = number1
        self.number2 = number2     # This is used to identify the numbers
    def plus(self):
        result = self.number1 + self.number2
        return result
    def minus(self):
        result = self.number1 - self.number2
        return result
    def multiply(self):
        result = self.number1 * self.number2
        return result
    def divide(self):
        result = self.number1 / self.number2
        return result              #Those four above are to describe the four operations (+ - * /)

def main():                        #Operating the calculator
    main = True
    while main == True:
        number1 = int(input("Put the 1st number:\n"))
        number2 = int(input("Put the 2nd number:\n"))
        operator = input("Put the operator:\n")
        wat = operator
        if operator == "+":
            result = number1 + number2
            print(result)
        elif operator == "-":
            result = number1 - number2
            print(result)
        elif operator == "*":
            result = number1 * number2
            print(result)
        elif operator == "/":
            result = number1 / number2
            print(result)

        Continue = input("Continue? [Y/N]\n")   #To exit the calculator
        if Continue == "N":
            run = False
            print("Goodbye")

main()