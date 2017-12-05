import re
str = "( or  (+ 55 977) 71)"

global leftParenCounter
leftParenCounter = 0
global rightParenCounter
rightParenCounter = 0


class Error(Exception):
    pass


class OperationError(Error):
    pass


class OperandError(Error):
    pass


def tokenize_str(input_str):
    new_str = input_str
    new_str = re.sub("or", "|", new_str, 0)
    new_str = re.sub("and", "&", new_str, 0)
    new_str = new_str.split()
    print(new_str)

    size = len(new_str)
    for i in range(1):
        if len(new_str[0]) > 1:
            if "(" is new_str[0][0]:
                k = new_str[0][0]
                m = new_str[0][1]
                new_list = {k, m}
                return new_list
            if new_str[0].isdigit():
                temp_list = []
                temp_list.append(new_str[0][:-1])


    return new_str



def prefixEval(op, op1, op2):
    if op is "+":
        return int(op1) + int(op2)
    elif op is "-":
        return int(op1) - int(op2)
    elif op is "*":
        return int(op1) * int(op2)
    elif op is "/":
        return int(op1) / int(op2)
    elif op is "&":
        x = int(op1)
        y = int(op2)
        z = x & y
        return z
    elif op is "|":
        x = int(op1)
        y = int(op2)
        z = x | y
        return z
    elif op is ">":
        return int(op1) > int(op2)
    elif op is "<":
        return int(op1) < int(op2)


def parseTokList(tok_list):
    global answer
    global leftParenCounter
    global rightParenCounter

    for i in range(1):
        if tok_list[i] is "(":
            leftParenCounter += 1
            tok_list.pop(0)
            answer = parseTokList(tok_list)
        if tok_list[i] is "-":
            op = tok_list.pop(0)
            op1 = parseTokList(tok_list)
            tok_list.pop(0)
            op2 = parseTokList(tok_list)
            tok_list.pop(0)
            return prefixEval(op, op1, op2)
        elif tok_list[i] is "+":
            op = tok_list.pop(0)
            op1 = parseTokList(tok_list)
            tok_list.pop(0)
            op2 = parseTokList(tok_list)
            tok_list.pop(0)
            return prefixEval(op, op1, op2)
        elif tok_list[i] is "*":
            op = tok_list.pop(0)
            op1 = parseTokList(tok_list)
            tok_list.pop(0)
            op2 = parseTokList(tok_list)
            tok_list.pop(0)
            return prefixEval(op, op1, op2)
        elif tok_list[i] is "/":
            op = tok_list.pop(0)
            op1 = parseTokList(tok_list)
            tok_list.pop(0)
            op2 = parseTokList(tok_list)
            tok_list.pop(0)
            return prefixEval(op, op1, op2)
        elif tok_list[i] is "&":
            op = tok_list.pop(0)
            op1 = parseTokList(tok_list)
            tok_list.pop(0)
            op2 = parseTokList(tok_list)
            tok_list.pop(0)
            return prefixEval(op, op1, op2)
        elif tok_list[i] is "|":
            op = tok_list.pop(0)
            op1 = parseTokList(tok_list)
            tok_list.pop(0)
            op2 = parseTokList(tok_list)
            tok_list.pop(0)
            return prefixEval(op, op1, op2)
        elif tok_list[i].isdigit():
            return tok_list[i]
        else:
            if tok_list[i] is ")":
                rightParenCounter += 1
                return answer
    if leftParenCounter == rightParenCounter:
        return answer


def prefixReader(str):
    print(">", str)
    temp_str = str.replace(" ", "")
    parens = re.search(r"\(\(", temp_str)
    if parens is not None:
        try:
            raise OperandError
        except OperandError:
            print("Expect operator after each left parenthesis")
    else:
        tok_list = tokenize_str(str)
        result = parseTokList(tok_list)
        print(">", result)


prefixReader(str)


