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

for i in range(len(operations)):
  newFirst = calculator(operations[i],numbers[0],numbers[1])
  del numbers[:2]
  numbers.insert(0, newFirst)

print(numbers)