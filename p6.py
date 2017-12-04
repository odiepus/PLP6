import re
str = "( or (+ 3 2) ( - 6 3))"

global lastLeftParen
lastLeftParen = False


class Error(Exception):
    pass

class OperationError(Error):
    pass

class OperandError(Error):
    pass



def tokenize_str(input_str):
    new_str = input_str.replace(" ", "")
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
    elif op is "and":
        return int(op1) & int(op2)
    elif op is "or":
        return int(op1) | int(op2)
    elif op is ">":
        return int(op1) > int(op2)
    elif op is "<":
        return int(op1) < int(op2)



def parseTokList(tok_list):
    global answer
    global lastLeftParen
    for i in tok_list:
        if i is "(":
            lastLeftParen = tok_list.pop(0)
            return parseTokList(tok_list)
        if i is "-":
            op = tok_list.pop(0)
            op1 = parseTokList(tok_list)
            tok_list.pop(0)
            op2 = parseTokList(tok_list)
            tok_list.pop(0)
            return prefixEval(op, op1, op2)
        elif i is "+":
            op = tok_list.pop(0)
            op1 = parseTokList(tok_list)
            tok_list.pop(0)
            op2 = parseTokList(tok_list)
            tok_list.pop(0)
            return prefixEval(op, op1, op2)
        elif i is "*":
            op = tok_list.pop(0)
            op1 = parseTokList(tok_list)
            tok_list.pop(0)
            op2 = parseTokList(tok_list)
            tok_list.pop(0)
            return prefixEval(op, op1, op2)
        elif i is "/":
            op = tok_list.pop(0)
            op1 = parseTokList(tok_list)
            tok_list.pop(0)
            op2 = parseTokList(tok_list)
            tok_list.pop(0)
            answer = prefixEval(op, op1, op2)
        elif i is "and":
            op = tok_list.pop(0)
            op1 = parseTokList(tok_list)
            tok_list.pop(0)
            op2 = parseTokList(tok_list)
            tok_list.pop(0)
            answer = prefixEval(op, op1, op2)
        elif i.isdigit():
            return i
        elif i is ")":
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


prefixReader(str)

