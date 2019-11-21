def is_digit(var):
    return var in ('0123456789')

def execute(numbers):
  if len(numbers) < 2:
    return numbers
  stack = []
  a = 0
  b = 0
  r = 0
  for i in numbers:
    if i == "+":
      a = stack.pop()
      b = stack.pop()
      r = b + a
      stack.append(r)
    elif i == "-":
      a = stack.pop()
      b = stack.pop()
      r = b - a
      stack.append(r)
    elif i == "*":
      a = stack.pop()
      b = stack.pop()
      r = b * a
      stack.append(r)
    elif i == "/":
      a = stack.pop()
      b = stack.pop()
      r = b / a
      stack.append(r)
    else:
      stack.append(i)
  print(stack)

def analyze(line):
    num = ""
    op = ""
    numbers = []
    operations = []
    line = line.replace(" ", "")
    line += "z"
    line = list(line)
    print(line)
    for i in range(len(line)):
      if(is_digit(line[i])):
        num += line[i]
        print(num)
      else:
        if num != "":
          numbers.append(int(num))
          num = ""
        op = line[i]
        operations.append(op)
        if len(operations) > 1 and operations[len(operations) - 1] == "-" or operations[len(operations) - 1] == "+":
          print("check order + -")
          if operations[len(operations) - 2] == "^" or operations[len(operations) - 2] == "/" or operations[len(operations) - 2] == "*":
            print('worng order')
            numbers.append(operations[len(operations) - 2])
            del operations[len(operations) - 2]
        if len(operations) > 1 and operations[len(operations) - 1] == "/" or operations[len(operations) - 1] == "*":
          print("check order: * /")
          if operations[len(operations) - 2] == "^":
            print('worng order')
            numbers.append(operations[len(operations) - 2])
            del operations[len(operations) - 2]
    operations.pop()
    print(numbers)
    print(operations)
    for i in operations:
      numbers.append(i)
    print(numbers)
    execute(numbers)




print('Whats the operation?')
expression = input()

analyze(expression)