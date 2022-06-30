def isOperator(a):
    if a != "": return (a in "+-*/")
    else: return False

def cheakPriority(a):
    if a in "+-": return 0
    if a in "*/": return 1
    
def isNumber(a):
    if a != "": return (a in "0123456789.")
    else: return False

def runOperator(op, number1, number2):
    if op == "+": return str(float(number1) + float(number2))
    if op == "-": return str(float(number1) - float(number2))
    if op == "*": return str(float(number1) * float(number2))
    if op == "/": return str(float(number1) / float(number2))

def Calculation(expr):
    expr = list(expr)
    stack_o = list()
    stack_n = list()
    num = ""
    while len(expr) > 0:
        a = expr.pop(0)
        if len(expr) > 0: d = expr[0]
        else: d = ""
        if isNumber(a):
            num += a
            if not isNumber(d):
                stack_n.append(num)
                num = ""
        elif isOperator(a):
            while True:
                if len(stack_o) > 0: top = stack_o[-1]
                else: top = ""
                if isOperator(top):
                    if not cheakPriority(a) > cheakPriority(top):
                        number2 = stack_n.pop()
                        op = stack_o.pop()
                        number1 = stack_n.pop()
                        stack_n.append(runOperator(op, number1, number2))
                    else:
                        stack_o.append(a)
                        break
                else:
                    stack_o.append(a)
                    break
        elif a == "(":
            stack_o.append(a)
        elif a == ")":
            while len(stack_o) > 0:
                a = stack_o.pop()
                if a == "(":
                    break
                elif isOperator(a):
                    number2 = stack_n.pop()
                    number1 = stack_n.pop()
                    stack_n.append(runOperator(a, number1, number2))

    while len(stack_o) > 0:
        a = stack_o.pop()
        if a == "(":
            break
        elif isOperator(a):
            number2 = stack_n.pop()
            number1 = stack_n.pop()
            stack_n.append(runOperator(a, number1, number2))

    return stack_n.pop()
