from tokens import *

class Token(object):

    def __init__(self,tip,vrednost):
        self.tip = tip
        self.vrednost = vrednost



class Lexer(object):

    def __init__(self,code):

        #niz karaktera za ulazni kod
        self.code = code
        self.pozicija = 0
        self.trenutni = code[self.pozicija]

    #pomera za jednu poziciju u nizu
    def next(self):

        self.pozicija += 1

        #provera za kraj koda

        if self.pozicija > len(self.code) - 1:
            self.trenutni = None #kraj
        else:
            self.trenutni = self.code[self.pozicija]


    def preskoci_space(self):
        while self.trenutni is not None and self.trenutni.isspace():
            self.next()


    def integer(self):
        """funkcija koja vraca integer
            koji se sastoji od vise cifara"""

        broj = ''

        while self.trenutni is not None and self.trenutni.isdigit():
            broj =+ self.trenutni
            self.next()

        return int(broj)


    def next_token(self):
        """glavna funkcija lexer-a koja
             vraca jedan(sledeci) token"""

        while self.trenutni is not None:

            if self.trenutni.isspace():
                self.preskoci_space()
                continue

            if self.trenutni.isdigit():
                return Token(INTEGER,self.integer())

            if self.trenutni == '+':
                self.next()
                return Token(PLUS,'+')

            if self.trenutni == '-':
                self.next()
                return Token(MINUS,'-')

            if self.trenutni == '/':
                self.next()
                return Token(PODELJENO,'/')

            if self.trenutni == '*':
                self.next()
                return Token(PUTA,'*')

            if self.trenutni == '(':
                self.next()
                return Token(LZ,'(')

            if self.trenutni == ')':
                self.next()
                return Token(DZ,')')


        return Token(EOF,None)






