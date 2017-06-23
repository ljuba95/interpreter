from lexer import Lexer
from parser import Parser

class Interpreter(object):

    def __init__(self,parsno_stablo):
        self.stablo = parsno_stablo

    def izvrsi(self):
        pass


def main():
    #text = input('prompt>')
    text = '2+5*3+(6-2)'
    lexer = Lexer(text)
    parser = Parser(lexer)
    interpreter = Interpreter(parser.parse())
    print(interpreter.izvrsi())



if __name__ == '__main__':
    main()