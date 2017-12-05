import re
str = "( + (+ 3 2) (- 7 3))"

global lastLeftParen
lastLeftParen = 0
global lastRightParen
lastRightParen = 0


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
    global lastLeftParen
    global lastRightParen
    for i in tok_list:
        if i is "(":
            lastLeftParen += 1
            tok_list.pop(0)
            answer = parseTokList(tok_list)
        elif i is "-":
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
            return prefixEval(op, op1, op2)
        elif i is "&":
            op = tok_list.pop(0)
            op1 = parseTokList(tok_list)
            tok_list.pop(0)
            op2 = parseTokList(tok_list)
            tok_list.pop(0)
            return prefixEval(op, op1, op2)
        elif i is "|":
            op = tok_list.pop(0)
            op1 = parseTokList(tok_list)
            tok_list.pop(0)
            op2 = parseTokList(tok_list)
            tok_list.pop(0)
            return prefixEval(op, op1, op2)
        elif i.isdigit():
            return i
        elif i is ")":
            lastRightParen += 1
            tok_list.pop(0)
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

