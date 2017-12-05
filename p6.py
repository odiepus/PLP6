#Program 6 by Hector Herrera kec296 UTSA


import re
import sys
#Used to keep track of parenthesis in our lines
global leftParenCounter
leftParenCounter = 0
global rightParenCounter
rightParenCounter = 0

# _____Exception Classes______ #
# Used to throw exceptions
# Depending on where the exception is thrown, the 'except' block will
# contain specific output to notify user of error

# Error class to use for user-defined exceptions
class Error(Exception):
    pass


# User-defined exception for function errors not covered by PrefixSyntax exception class
class FunctionError(Error):
    pass

# User-defined exception class to notify user of improper input format
class PrefixSyntax(Error):
    pass

# Function used to eval an operation on its two operands.
# Series of if statements are used since there in no switch equivalent in python
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
        if isinstance(op2, (bool)):
            y = op2
        elif op2.isdigit():
            y = int(op2)
        z = x & y
        return z
    elif op is "|":
        if isinstance(op1, (bool)):
            x = op1
        elif op1.isdigit():
            x = int(op1)
        if isinstance(op2, (bool)):
            y = op2
        elif op2.isdigit():
            y = int(op2)
        z = x | y
        return z
    elif op is ">":
        return int(op1) > int(op2)
    elif op is "<":
        return int(op1) < int(op2)

# Function used to parse the input line and extract the operator and its two operands
# It calls itself recursively using a for-loop. This my hacky way of using a switch in python

# This is ugly!!!! More time would be required to modularize it since each if
# statement has repeat code
# In each if statement i check if I am at the start of an operation
# If so, then count the parenthesis, remove the element and call this function passing in
# the the modified list.
# Next I look for correct operand, remove it from list, then look for operands.
# Operands are found by calling this function with newly modified list.
# When operands are found the function returns it and the element is removed from list.
# With operator and operands found the prefixEval function is called and the result is returned
# I continue to parse the list looking for closing parenthesis. When the list is empty
# if the left parenthesis and the right parenthesis are equal then return the result
# otherwise throw exception and move on to next input
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

# Function used to remove or insert spaces, catch non-ints, look out for format errors and send
# a clean list to parseTokList() for operations
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

# Function uses Professor Clark's user-input algorithm from Lecture03
# For each input line prefixReader() is called with each line passed into the function
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

# start the program loop
start()
