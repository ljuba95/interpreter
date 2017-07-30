from tokens import *
from ast import *

#morao sam da reimenujem file jer python ima built-in module parser, posle sat vremena debug-a -.-

class Parser(object):

    """
    Gramatika:
    
    program -> compound_statement TACKA
    
    compound_statement -> BEGIN statement_list END
    
    statement_list -> statement | statement SEMI statement_list
    
    statement -> compound_statement | assign_statement | empty
    
    empty ->
    
    assign_statement -> promenljiva ASSIGN izraz
    
    izraz -> term ((PLUS | MINUS) term)*
    
    term -> faktor ((PUTA | PODELJENO) faktor)*
    
    faktor -> (PLUS | MINUS) faktor | INTEGER | LZ izraz DZ | promenljiva
    
    promenljiva -> ID
    
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

    def program(self):
        """
        program pravilo gramatike.
        Glavna funkcija koja vraca parsno stablo.
        :return: AST root
        """

        cvor = self.compound_statement()
        self.move(TACKA)
        return cvor

    def compound_statement(self):
        """
        compound_statement pravilo gramatike impl.
        Vraca Compound cvor koji sadrzi listu statement-a.
        :return: Compound node
        """

        self.move(BEGIN)
        stmt_list = self.statement_list()
        self.move(END)

        koren = Compound()

        for stmt in stmt_list:
            koren.deca.append(stmt)

        return koren

    def statement_list(self):
        """
        statement_list pravilo gramatike impl.
        Vraca listu statement-a u okviru jednog begin-end bloka.
        :return: statement list
        """

        lista = [self.statement()]

        while self.trenutni_token.tip == SEMI:
            self.move(SEMI)
            lista.append(self.statement())

        return lista

    def statement(self):
        """
        statement pravilo gramatike impl.
        Vraca cvor(compound, assign ili empty)
        """

        if self.trenutni_token.tip == BEGIN:
            cvor = self.compound_statement()
        elif self.trenutni_token.tip == ID:
            cvor = self.assign_statement()
        else:
            cvor = self.empty()

        return cvor

    def assign_statement(self):
        """
        assign_statement pravilo gramatike impl.
        Vraca cvor tipa Assign(ex. a := 5)
        :return: Assign Node
        """

        var = self.promenljiva()
        token = self.trenutni_token
        self.move(ASSIGN)
        izraz = self.izraz()

        return Assign(var,token,izraz)

    def promenljiva(self):
        """
        promenljiva pravilo gramatike impl.
        Vraca cvor tipa Var
        :return: Var Node
        """

        cvor = Var(self.trenutni_token)
        self.move(ID)
        return cvor

    def empty(self):
        """
        empty pravilo gramatike impl.
        Vraca NoOp cvor(ex 'BEGIN END.' je validan program).
        :return: NoOp Node
        """

        return NoOp()


    def faktor(self):
        """
        Implementacija "faktor" pravila gramatike.
        :return: cvor tipa UnarnaOperacija, 
        cvor tipa Broj ili koren podstabla koje predstavlja "izraz"
        """
        token = self.trenutni_token
        if token.tip == PLUS:
            self.move(PLUS)
            return UnarnaOperacija(token,self.faktor())
        elif token.tip == MINUS:
            self.move(MINUS)
            return UnarnaOperacija(token,self.faktor())
        elif token.tip == INTEGER:
            self.move(INTEGER)
            return Broj(token)
        elif token.tip == LZ:
            self.move(LZ)
            cvor = self.izraz()
            self.move(DZ)
            return cvor
        elif token.tip == ID:
            return self.promenljiva()

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
        return self.program()