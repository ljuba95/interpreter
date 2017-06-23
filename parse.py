from tokens import *
from ast import *

#morao sam da reimenujem file jer python ima built-in module parser, posle sat vremena debug-a -.-

class Parser(object):

    """
    
    Gramatika:
    
    izraz -> term ((PLUS | MINUS) term)*
    term -> faktor ((PUTA | PODELJENO) faktor)*
    faktor -> INTEGER | LZ izraz DZ
    """

    def __init__(self,lexer):
        self.lexer = lexer
        self.trenutni_token = self.lexer.next_token() #inicijalizacija prvog tokena

    def greska(self):
        raise Exception('Greska pri parsiranju na {}.'.format(self.trenutni_token))


    def move(self,token):
        """
        Pomera se na sledeci token.
        :param token: tip trenutnog tokena
        """
        if self.trenutni_token.tip == token:
            self.trenutni_token = self.lexer.next_token()
        else:
            self.greska()

    def faktor(self):
        """
        Implementacija "faktor" pravila gramatike.
        :return: cvor tipa Broj ili koren podstabla koje predstavlja "izraz"
        """
        token = self.trenutni_token
        if token.tip == INTEGER:
            self.move(INTEGER)
            return Broj(token)
        elif token.tip == LZ:
            self.move(LZ)
            cvor = self.izraz()
            self.move(DZ)
            return cvor

    def term(self):
        """
        Implementacija "term" pravila gramatike.
        :return: koren podstabla koje predstavlja "term"
        """

        cvor = self.faktor()

        while self.trenutni_token.tip == PUTA or self.trenutni_token.tip == PODELJENO:
            token = self.trenutni_token
            if token.tip == PUTA:
                self.move(PUTA)
            else:
                self.move(PODELJENO)

            cvor = BinarnaOperacija(cvor,token,self.faktor())

        return cvor

    def izraz(self):
        """
        Implementacija "izraz" pravila gramatike.
        :return: koren podstabla koje predstavlja "izraz"
        """

        cvor = self.term()

        while self.trenutni_token.tip == PLUS or self.trenutni_token.tip == MINUS:
            token = self.trenutni_token
            if token.tip == PLUS:
                self.move(PLUS)
            else:
                self.move(MINUS)

            cvor = BinarnaOperacija(cvor,token,self.term())

        return cvor


    def parse(self):
        return self.izraz()