import re
str = "( +  3 3)"

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
    new_str = input_str.replace(" ", "")
    new_str = new_str.replace("or", "|")
    new_str = new_str.replace("and", "&")
    temp_tok = re.findall(r"([^.])|[.]", new_str)
    return temp_tok


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
        return x & y
    elif op is "|":
        x = int(op1)
        y = int(op2)
        return x | y
    elif op is ">":
        return int(op1) > int(op2)
    elif op is "<":
        return int(op1) < int(op2)



def parseTokList(tok_list):
    global answer
    global leftParenCounter
    global rightParenCounter
    for i in range(len(tok_list)):
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
            prefixEval(op, op1, op2)
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
                tok_list.pop(0)
    if leftParenCounter == rightParanCounter:
        return answer

def prefixReader(str):
    print(">", str)
    str = str.replace(" ", "")
    parens = re.search(r"\(\(", str)
    if parens is not None:
        try:
            raise OperandError
        except OperandError:
            print("Expect operator after each left parenthesis")
    else:
        tok_list = tokenize_str(str)
        result = parseTokList(tok_list)
        print(result)
        print(3 | 4)


prefixReader(str)


