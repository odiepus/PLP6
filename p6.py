import re
import sys

str = "(+ (- 5 3)(+ 3 9))"

global leftParenCounter
leftParenCounter = 0
global rightParenCounter
rightParenCounter = 0
global new_list
new_list = []


class Error(Exception):
    pass


class FunctionError(Error):
    pass


class PrefixSyntax(Error):
    pass


def tokenize_str(new_str):
    global new_list
    for i in range(1):
        if len(new_str) == 0:
            return new_list
        if len(new_str[0]) == 1:
            new_list.append(new_str.pop(0))
            tokenize_str(new_str)
            if len(new_str) == 0:
                return new_list
        if len(new_str[0]) > 1:
            query_re = re.compile(r"\)\s")
            match_obj = query_re.search(new_str[0])
            another_re = re.compile(r'\)\(')
            another_match = another_re.search(new_str[0])
            if len(new_str) == 0:
                return new_list
            if "(" is new_str[0][0]:
                temp_str = new_str[0]
                new_str.pop(0)
                new_list.append(temp_str[0])
                new_list.append(temp_str[1:])
                tokenize_str(new_str)
                if len(new_str) == 0:
                    return new_list
            if match_obj is not None:
                    temp_str = new_str[0]
                    new_str.pop(0)
                    new_list.append(temp_str[:-1])
                    new_list.append(temp_str[-1])
                    tokenize_str(new_str)
                    if len(new_str) == 0:
                        return new_list
            if another_match is not None:
                temp_str = new_str[0]
                new_str.pop(0)
                temp_str = temp_str.replace(")(", ") (", 1)
                temp_list = temp_str.split()
                new_list.append(temp_list[0][:-1])
                new_list.append(temp_list[0][-1])
                new_list.append(temp_list[1][:-1])
                new_list.append(temp_list[1][-1])
                tokenize_str(new_str)
                if len(new_str) == 0:
                    return new_list

            else:
                if len(new_str) == 0:
                    return new_list
                new_list.append(new_str.pop(0))
                tokenize_str(new_str)
                if len(new_str) == 0:
                    return new_list


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
            if len(tok_list) is 0:
                try:
                    raise PrefixSyntax
                except PrefixSyntax:
                    print("Missing ending parenthesis")


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
        elif len(tok_list) != 0:
            if tok_list[i] is ")":
                rightParenCounter += 1
                tok_list.pop(0)
                if len(tok_list) is 0:
                    if leftParenCounter == rightParenCounter:
                        return answer
                    else:
                        try:
                            raise PrefixSyntax
                        except PrefixSyntax:
                            print("Missing ending parenthesis")

    if leftParenCounter == rightParenCounter:
        return answer
    else:
        try:
            raise PrefixSyntax
        except PrefixSyntax:
            print("Missing parenthesis!!!\Check your parenthesis.")



def prefixReader(str):
    print(">", str)
    temp_str = str.replace(" ", "")
    parens = re.search(r"\(\(", temp_str)
    if parens is not None:
        try:
            raise PrefixSyntax
        except PrefixSyntax:
            print("Expect operator after each left parenthesis")
    else:
        new_str = str
        new_str = re.sub("or", "|", new_str, 0)
        new_str = re.sub("and", "&", new_str, 0)
        new_str = new_str.split()
        tok_list = tokenize_str(new_str)
        result = parseTokList(tok_list)
        print(">", result)


prefixReader(str)
# while True:
#     print("#args=", len(sys.argv))
#     if len(sys.argv) < 2:
#         print("filename needed as command argument")
#         sys.exit(1)
#     file = open(sys.argv[1], "r")
#     while True:
#         inputLine = file.readline() # reads one text line from the file
#         # check for no input (i.e., EOF)
#         if inputLine == "":
#             break
#         inputLine = inputLine.rstrip('\n')  # remove the newline
#         print(inputLine)
#
#         try:
#             prefixReader(str)
#         except FunctionError:
#             print("Function prefixReader() threw an exception")
#
#
#     file.close()
