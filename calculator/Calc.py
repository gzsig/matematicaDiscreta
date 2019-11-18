def expr(): # calculating expression
    res = item()
    global index
    global stripExpression
    while (index < len(stripExpression) and (stripExpression[index] == "+" or stripExpression[index] == "-")):
        index += 1
        if index < len(stripExpression):
            if (stripExpression[index - 1] == "+"):
                res += item()
            else:
                res -= item()
        else:
            print("Incorrect expression: there is no number after the operator")
            exit(0)
    return res

def item(): #calculating individual operation
    res = mult()
    global index
    global stripExpression
    while (index < len(stripExpression) and (stripExpression[index] == "*" or stripExpression[index] == "/")):
        index += 1
        if (stripExpression[index - 1] == "*"):
            res *= mult()
        else:
            denominator = mult()
            try:
                res /= denominator
            except ZeroDivisionError:
                print("Division by zero!")
                exit(0)
    return res

def mult(): #calculating multiplier
    res = 0
    global index
    global stripExpression
    if (stripExpression[index] == "("): #calculating expression in the parentheses
        index += 1
        res = expr()
        if index >= len(stripExpression) or stripExpression[index] != ")":
            print("Expression doesn't have a close parentheses!")
            exit(0)
        index += 1
    else:
        if (stripExpression[index] == "-"): # checking for negative multipliers
            index += 1
            res = (-1) * mult()
        else:
            number = "" #extracting a number from expression adding a dor if it is a float number
            if stripExpression[index] == ".":
                print("Number must start with a digit!")
                exit(0)
            while (index < len(stripExpression) and ((stripExpression[index] >= "0" and stripExpression[index] <= "9") or stripExpression[index] == ".")):
                number += stripExpression[index]
                index += 1
            try:
                res = float(number)
            except ValueError:
                print("Incorrect number in the input = " + number)
                exit(0)
    return res

while True:
     try:
        expression = input()
     except EOFError:
         exit(0)
     stripExpression = expression.replace(" ", "")
     str = "1234567890-+*/()"
     for i in stripExpression:
         if i not in str:
             print("Incorrect character in the input = " + i)
             exit(0)
     index = 0
     print(expr())