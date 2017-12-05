import re
import sys

str = "( / ( + 3 5 )  ) "

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
        if isinstance(op1, (bool)):
            x = op1
        elif op1.isdigit():
            x = int(op1)
        else:
            try:
                raise FunctionError
            except FunctionError:
                print("Operand is neither a boolean or integer: cannot eval &")
        if isinstance(op2, (bool)):
            y = op2
        elif op2.isdigit():
            y = int(op2)
        else:
            try:
                raise FunctionError
            except FunctionError:
                print("Operand is neither a boolean or integer: cannot eval &")
        z = x & y
        return z
    elif op is "|":
        if isinstance(op1, (bool)):
            x = op1
        elif op1.isdigit():
            x = int(op1)
        else:
            try:
                raise FunctionError
            except FunctionError:
                print("Operand is neither a boolean or integer: cannot eval &")
        if isinstance(op2, (bool)):
            y = op2
        elif op2.isdigit():
            y = int(op2)
        else:
            try:
                raise FunctionError
            except FunctionError:
                print("Operand is neither a boolean or integer: cannot eval &")
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
            if tok_list[i] is not ")":
                if tok_list[i] is not "(":
                    tok_list.pop(0)
            if tok_list[i] is ")":
                try:
                    raise PrefixSyntax
                except PrefixSyntax:
                    print("Missing operand")
                    return
            op2 = parseTokList(tok_list)
            if tok_list[i] is not ")":
                if tok_list[i] is not "(":
                    tok_list.pop(0)
            if tok_list[i].isdigit():
                try:
                    raise PrefixSyntax
                except PrefixSyntax:
                    print("Extra operand")
                    return
            return prefixEval(op, op1, op2)
        elif tok_list[i] is "+":
            op = tok_list.pop(0)
            op1 = parseTokList(tok_list)
            if tok_list[i] is not ")":
                if tok_list[i] is not "(":
                    tok_list.pop(0)
            if tok_list[i] is ")":
                try:
                    raise PrefixSyntax
                except PrefixSyntax:
                    print("Missing operand")
                    return
            op2 = parseTokList(tok_list)
            if tok_list[i] is not ")":
                if tok_list[i] is not "(":
                    tok_list.pop(0)
            return prefixEval(op, op1, op2)
        elif tok_list[i] is "*":
            op = tok_list.pop(0)
            op1 = parseTokList(tok_list)
            if tok_list[i] is not ")":
                if tok_list[i] is not "(":
                    tok_list.pop(0)
            if tok_list[i] is ")":
                try:
                    raise PrefixSyntax
                except PrefixSyntax:
                    print("Missing operand")
                    return
            op2 = parseTokList(tok_list)
            if tok_list[i] is not ")":
                if tok_list[i] is not "(":
                    tok_list.pop(0)
            return prefixEval(op, op1, op2)
        elif tok_list[i] is "/":
            op = tok_list.pop(0)
            op1 = parseTokList(tok_list)
            if tok_list[i] is not ")":
                if tok_list[i] is not "(":
                    tok_list.pop(0)
            if tok_list[i] is ")":
                try:
                    raise PrefixSyntax
                except PrefixSyntax:
                    print("Missing operand")
                    return
            op2 = parseTokList(tok_list)
            if tok_list[i] is not ")":
                if tok_list[i] is not "(":
                    tok_list.pop(0)
            return prefixEval(op, op1, op2)
        elif tok_list[i] is "&":
            op = tok_list.pop(0)
            op1 = parseTokList(tok_list)
            if tok_list[i] is not ")":
                if tok_list[i] is not "(":
                    tok_list.pop(0)
            if tok_list[i] is ")":
                try:
                    raise PrefixSyntax
                except PrefixSyntax:
                    print("Missing operand")
                    return
            op2 = parseTokList(tok_list)
            if tok_list[i] is not ")":
                if tok_list[i] is not "(":
                    tok_list.pop(0)
            return prefixEval(op, op1, op2)
        elif tok_list[i] is "|":
            op = tok_list.pop(0)
            op1 = parseTokList(tok_list)
            if tok_list[i] is not ")":
                if tok_list[i] is not "(":
                    tok_list.pop(0)
            if tok_list[i] is ")":
                try:
                    raise PrefixSyntax
                except PrefixSyntax:
                    print("Missing operand")
                    return
            op2 = parseTokList(tok_list)
            if tok_list[i] is not ")":
                if tok_list[i] is not "(":
                    tok_list.pop(0)
            return prefixEval(op, op1, op2)
        elif tok_list[i] is ">":
            op = tok_list.pop(0)
            op1 = parseTokList(tok_list)
            if tok_list[i] is not ")":
                if tok_list[i] is not "(":
                    tok_list.pop(0)
            if tok_list[i] is ")":
                try:
                    raise PrefixSyntax
                except PrefixSyntax:
                    print("Missing operand")
                    return
            op2 = parseTokList(tok_list)
            if tok_list[i] is not ")":
                if tok_list[i] is not "(":
                    tok_list.pop(0)
            return prefixEval(op, op1, op2)
        elif tok_list[i] is "<":
            op = tok_list.pop(0)
            op1 = parseTokList(tok_list)
            if tok_list[i] is not ")":
                if tok_list[i] is not "(":
                    tok_list.pop(0)
            if tok_list[i] is ")":
                try:
                    raise PrefixSyntax
                except PrefixSyntax:
                    print("Missing operand")
                    return
            op2 = parseTokList(tok_list)
            if tok_list[i] is not ")":
                if tok_list[i] is not "(":
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
                elif len(tok_list) is not 0:
                    return answer
            else:
                try:
                    raise PrefixSyntax
                except PrefixSyntax:
                    print("Invalid operand")
                    return

def prefixReader(str):
    temp_str = str.replace(" ", "")
    bad_start = re.search(r"^\(", temp_str)
    parens = re.search(r"\(\(", temp_str)
    if bad_start is None:
        try:
            raise PrefixSyntax
        except PrefixSyntax:
            print("Must use parenthesis")
            return
    elif parens is not None:
        try:
            raise PrefixSyntax
        except PrefixSyntax:
            print("Expect operator after each left parenthesis")
            return
    else:
        new_str = str
        new_str = re.sub("or", "|", new_str, 0)
        new_str = re.sub("and", "&", new_str, 0)
        new_str = re.sub(r'\)', ') ', new_str)
        new_str = re.sub(r'\)', ' )', new_str)
        new_str = re.sub(r'\(', '( ', new_str)
        print(">", new_str)
        another_check = re.findall(r'(\s\d+){3,}\s\)', new_str)
        if len(another_check) is not 0:
            try:
                raise PrefixSyntax
            except PrefixSyntax:
                print("Too many operands")
                return
        another_check_1 = re.findall(r'[+-]\s\d+\s\)', new_str)
        if len(another_check_1) is not 0:
            try:
                raise PrefixSyntax
            except PrefixSyntax:
                print("Too few operands")
                return
        another_check_2 = re.findall(r'\d+\s[+*/&|><-]\s\d+', new_str)
        if len(another_check_2) is not 0:
            try:
                raise PrefixSyntax
            except PrefixSyntax:
                print("Missing parenthesis")
                return
        new_str = new_str.split()
        for i in new_str:
            if i.isalpha():
                try:
                    raise PrefixSyntax
                except PrefixSyntax:
                    print("Operands must be of type int\nOperators must be [ + - * / and/& or/| > <]")
                    return
        result = parseTokList(new_str)
        print(">", result)


# try:
#  prefixReader(str)
# except FunctionError:
#  print("Function prefixReader() threw an exception")


def start():
    lines = []
    print("#args=", len(sys.argv))
    if len(sys.argv) < 2:
        print("filename needed as command argument")
        sys.exit(1)
    file = open(sys.argv[1], "r")
    while True:
        inputLine = file.readline()  # reads one text line from the file
        # check for no input (i.e., EOF)
        if inputLine == "":
            break
        inputLine = inputLine.rstrip('\n')  # remove the newline
        lines.append(inputLine)

    file.close()

    for i in lines:
        try:
            prefixReader(i)
        except FunctionError:
            print("Function prefixReader() threw an exception")

start()
