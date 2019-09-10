def is_digit(var):
    return var in ('0123456789')

def validate(line):
    line = line.replace(" ", "")
    line = list(line)
    for element in line:
        if element not in ('0123456789/*+-^()'):
            print("not here")
            return False
    return True


def operators(operation, num1, num2):
    if operation == '+':
        return num1 + num2
    if operation == '-':
        return num1-num2
    if operation == '*':
        return num1*num2
    if operation == '/':
        return num1/num2
    if operation == '^':
        return num1 ** num2


def arrayManipulation(index, operations, numbers):
    newNum = operators(operations[index], numbers[index], numbers[index+1])
    del operations[index]
    del numbers[index+1]
    del numbers[index]
    numbers.insert(index, newNum)


def calculator(numbers, operations, j):
    for i in range(j):
        if "^" in operations:
            print("vou ^")
            index = operations.index("^")
            arrayManipulation(index, operations, numbers)
        elif "*" in operations or "/" in operations:
            mult = j
            div = j
            if "*" in operations:
                mult = operations.index("*")
            if "/" in operations:
                div = operations.index("/")
            if mult < div:
                print("vou *")
                index = mult
                arrayManipulation(index, operations, numbers)
            else:
                print("vou /")
                index = operations.index("/")
                arrayManipulation(index, operations, numbers)
        elif "+" in operations:
            print("vou +")
            index = operations.index("+")
            arrayManipulation(index, operations, numbers)
        elif "-" in operations:
            print("vou -")
            index = operations.index("-")
            arrayManipulation(index, operations, numbers)


def analyze(numbers, line):
    num = ""
    op = ""

    operations = []
    result = []

    line = line.replace(" ", "")
    line += "z"
    line = list(line)
    print(line)
    for i in range(len(line)):
        if(is_digit(line[i])):
            num += line[i]
            print(num)
        else:
            numbers.append(int(num))
            num = ""
            op = line[i]
            operations.append(op)
    operations.pop()

    print(numbers)
    print(operations)

    j = len(operations)

    calculator(numbers, operations, j)


print("please type your operation:")
line = input()
if validate(line):
    numbers = []
    analyze(numbers, line)
    print(numbers[0])
else:
    print("error")
