print("Enter a bracket expression:")
input_str = input()
input_str += '#'
i = 0
sym = 'a'
signs = "+-*/"
letters = "abcdefghijklmnopqrstuvwxyz"


def Letter(sym):
    if sym in letters:
        return 1
    else:
        return 0

def Sign(sym):
    if sym in signs:
        return 1
    else:
        return 0

class ParseError(Exception):
    def __init__(self):
        print('error')


def error():
    raise ParseError()

def read():
    global sym, i
    i += 1
    sym = input_str[i]

class MainClass():

    def new_lang(self):
        self.lang()
        if (sym == '#'):
            return
        error()

    def lang(self):
        if Letter(sym):
            read()
            self.end()
        elif sym == '{':
            read()
            self.in_brackets()
            if (sym == '}'):
                read()
            else:
                error()
            self.square()
        elif sym == '[':
            read()
            self.in_brackets()
            if (sym == ']'):
                read()
            else:
                error()
            self.circle()
        elif sym == '(':
            read()
            self.in_brackets()
            if (sym == ')'):
                read()
            else:
                error()
            self.curly()

    def end(self):
        if Sign(sym):
            read()
            if Letter(sym):
                read()
                self.end()
            else:
                error()

    def in_brackets(self):
        if Letter(sym):
            read()
            self.end()
        elif sym == '{':
            read()
            self.in_brackets()
            if (sym == '}'):
                read()
            else:
                error()
            if Sign(sym):
                read()
                if sym == '[':
                    read()
                    self.in_brackets()
                    if (sym == ']'):
                        read()
                    else:
                        error()
                    self.circle()
                else:
                    error()
            else:
                error()
        elif sym == '[':
            read()
            self.in_brackets()
            if (sym == ']'):
                read()
            else:
                error()
            if Sign(sym):
                read()
                if sym == '(':
                    read()
                    self.in_brackets()
                    if (sym == ')'):
                        read()
                    else:
                        error()
                    self.curly()
                else:
                    error()
            else:
                error()
        elif sym == ')':
            read()
            self.in_brackets()
            if (sym == '}'):
                read()
            else:
                error()
            if Sign(sym):
                read()
                if sym == '{':
                    read()
                    self.in_brackets()
                    if (sym == '}'):
                        read()
                    else:
                        error()
                    self.square()
                else:
                    error()
            else:
                error()
        else:
            error()

    def square(self):
        if Sign(sym):
            read()
            if sym == "[":
                read()
                self.in_brackets()
                if sym == "]":
                    read()
                    self.circle()
                else:
                    error()
            else:
                error()

    def circle(self):
        if Sign(sym):
            read()
            if sym == "(":
                read()
                self.in_brackets()
                if sym == ")":
                    read()
                    self.curly()
                else:
                    error()
            else:
                error()

    def curly(self):
        if Sign(sym):
            read()
            if sym == "{":
                read()
                self.in_brackets()
                if sym == "}":
                    read()
                    self.square()
                else:
                    error()
            else:
                error()


def main():
    global sym
    sym = input_str[0]
    m = MainClass()
    try:
        m.new_lang()
    except ParseError:
        print('false')
        return
    print('true')


main()
input("press any key to exit...")
