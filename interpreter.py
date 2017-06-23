
from parse import Parser
from lexer import Lexer
from ast import *

class Interpreter(object):

    def __init__(self,parsno_stablo):
        self.stablo = parsno_stablo


    def izvrsi(self):
        pass


def prikazLKD(koren):
    if koren is None:
        return

    if type(koren) is BinarnaOperacija:
        prikazLKD(koren.levo)

        print(koren)
        prikazLKD(koren.desno)
    else:
        print(koren)

def main():
    #text = input('prompt>')
    text = '2+5*3+(3+5)/2'
    lexer = Lexer(text)
    parser = Parser(lexer)
    interpreter = Interpreter(parser.parse())

    prikazLKD(interpreter.stablo)



if __name__ == '__main__':
    main()