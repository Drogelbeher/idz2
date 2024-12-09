import sys
def letter(sym):
    if sym in letters:
        return 1
    else:
        return 0

class ParseError(Exception):
    def __init__(self):
        print('Error')

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
            return error()

    def lang(self):
        if letter(sym):
            read()
            if sym == '=':
                read()
                if sym == '>':
                    read()
                else:
                    error()
            else:
                error()
            self.ending()
        else:
            error()
            
    def ending(self):
        if letter(sym):
            read()
            self.end()
        elif sym == '(':
            read()
            if letter(sym):
                read()
                if sym == '=':
                    read()
                    if sym == '>':
                        read()
                        self.ending()
                        if sym == ')':
                            read()
                            self.end()
                        else:
                            error()
                    else:
                        error()
                else:
                    error()
            else:
                error()
        else:
            error()

    def end(self):
        if sym == '=':
            read()
            if sym == '>':
                read()
                self.ending()
            else:
                error()
        elif sym == '#':
            print("Succes")
            sys.exit()
        elif sym == ")":
            pass
        else:
            error()
def main():
    print("Enter an expression with an implication:")
    global sym, letters, i, input_str, m
    i = 0
    letters = "abcdefghijklmnopqrstuvwxyz"
    input_str = input()
    input_str += '#'
    sym = input_str[0]
    m = MainClass()
    try:
        m.new_lang()
    except ParseError:
        print("You entered the wrong expression")
main()
