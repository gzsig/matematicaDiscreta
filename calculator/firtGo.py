# https://codereview.stackexchange.com/questions/46698/small-python-calculator
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
    print(numbers)
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
    return numbers
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
    return calculator(numbers, operations, j)

def innerCalc(pairs, line):
    for i in range(len(pairs)):
        print('\n')
        print('VOU COMECAR O LOOP: ' + str(i) + "\n")
        openKey = pairs[i][0]
        closeKey = pairs[i][1]
        # print(openKey)
        # print(closeKey)
        innerOperation = line[openKey+1:closeKey]
        print("operation: " + innerOperation)
        innerRes = analyze([],innerOperation)
        print("oque eu retorno??")
        print(innerRes)
        line = list(line)
        del line[openKey]
        line.insert(openKey, str(innerRes[0]))
        print("salvei")
        # print(line)
        cont = openKey+1
        while cont <= closeKey:
            del line[cont]
            line.insert(cont, " ")
            cont += 1
        line = "".join(line)
        print("current line: " + line)
    return line
def handelParen(line):
        iOpen = []
        # contOpen = 0
        iClose = []
        # contClose = 0
        pairs = []
        print("tenho ()")
        arr = list(line)
        for i in range(len(arr)):
            if arr[i] == "(":
                iOpen.append(i)
                # contOpen+=1
            if arr[i] == ")":
                iClose.append(i)
                # contClose += 1
        print(iOpen)
        print(iClose)

        a=0
        j=1

        while a < len(iOpen)-1:
            while j <len(iOpen):
                if iOpen[j] > iClose[a]:
                    pairs.append([iOpen[j-1],iClose[a]])
                    del iOpen[j-1]
                    del iClose[a]
                j+=1
            a += 1
        print(pairs)

        print(iOpen)
        print(iClose)

        z =0
        iClose.reverse()
        while z < len(iOpen):
            pairs.append([iOpen[z],iClose[z]])
            del iOpen[z]
            del iClose[z]
        print(pairs)

        for j in range(len(pairs)):
            for i in range(len(pairs)-j-1):
                if (pairs[i][1] - pairs[i][0]) > (pairs[i+1][1] - pairs[i+1][0]):
                    
                    pairs[i], pairs[i+1] = pairs[i+1], pairs[i]

        print(pairs)
        print(line)
        return innerCalc(pairs, line)
print("please type your operation:")
line = input()
if validate(line):
    if ("(" in line) & (")" in line):
        line = "("+ line + ")"
        res = handelParen(line)
        print("\n\n\n RESTPOSTA:" + res)

    else:
        numbers = []
        analyze(numbers, line)
        print(numbers[0])
else:
    print("error")
