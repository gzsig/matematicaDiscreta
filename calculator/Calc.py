def is_digit(var):
    return var in ('0123456789')


def calculator(operation, num1, num2):
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


print("please type your operation:")
num = ""
op = ""

numbers = []
operations = []
result = []

line = input()
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

for i in range(j):
    if "*" in operations:
        print("vou *")
        index = operations.index("*")
        newNum = calculator(operations[index], numbers[index], numbers[index+1])
        del operations[index]
        del numbers[index+1]
        del numbers[index]
        numbers.insert(index, newNum)
    elif "/" in operations:
        print("vou /")
        index = operations.index("/")
        newNum = calculator(operations[index], numbers[index], numbers[index+1])
        del operations[index]
        del numbers[index+1]
        del numbers[index]
        numbers.insert(index, newNum)
    elif "+" in operations:
        print("vou +")
        index = operations.index("+")
        newNum = calculator(operations[index], numbers[index], numbers[index+1])
        del operations[index]
        del numbers[index+1]
        del numbers[index]
        numbers.insert(index, newNum)
    elif "-" in operations:
        print("vou -")
        index = operations.index("-")
        newNum = calculator(operations[index], numbers[index], numbers[index+1])
        del operations[index]
        del numbers[index+1]
        del numbers[index]
        numbers.insert(index, newNum)

print(numbers)
