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