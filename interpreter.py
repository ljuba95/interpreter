
from parse import Parser
from lexer import Lexer
from tokens import *
from ast import *

class Visitor(object):

    def poseti(self,cvor):
        """
        Dispatcher metoda koja zove odgovarajucu metodu interpretera
        u zavisnosti od tipa cvor-a.
        :param cvor: trenutni cvor
        :return: odgovarajuca metoda
        """
        return getattr(self,'poseti_' + type(cvor).__name__)(cvor)

class Interpreter(Visitor):

    GLOBAL = {}

    def __init__(self,parser):
        self.parser = parser
        self.stablo = parser.parse()

    #metode za evaluaciju cvorova ast-a po visitor pattern-u

    def poseti_Compound(self,cvor):
        for dete in cvor.deca:
            self.poseti(dete)

    def poseti_NoOp(self,cvor):
        pass

    def poseti_Assign(self,cvor):
        ime = cvor.levo.vrednost
        self.GLOBAL[ime] = self.poseti(cvor.desno)

    def poseti_Var(self,cvor):
        ime = cvor.vrednost
        vrednost = self.GLOBAL.get(ime)

        if vrednost is None:
            raise NameError(repr(ime))
        else:
            return vrednost

    def poseti_BinarnaOperacija(self,cvor):
        if cvor.operacija.tip == PLUS:
            return self.poseti(cvor.levo) + self.poseti(cvor.desno)
        if cvor.operacija.tip == MINUS:
            return self.poseti(cvor.levo) - self.poseti(cvor.desno)
        if cvor.operacija.tip == PUTA:
            return self.poseti(cvor.levo) * self.poseti(cvor.desno)
        if cvor.operacija.tip == PODELJENO:
            return self.poseti(cvor.levo) / self.poseti(cvor.desno)

    def poseti_UnarnaOperacija(self,cvor):
        if cvor.operacija.tip == PLUS:
            return self.poseti(cvor.izraz)
        else:
            return -self.poseti(cvor.izraz)


    def poseti_Broj(self,cvor):
        return cvor.token.vrednost

    def izvrsi(self):
        return self.poseti(self.stablo)


def prikazLKD(koren):
    if koren is None:
        return

    if type(koren) is BinarnaOperacija:
        prikazLKD(koren.levo)
        print(koren)
        prikazLKD(koren.desno)
    elif type(koren) is UnarnaOperacija:
        print(koren)
        prikazLKD(koren.izraz)
    else:
        print(koren)



def main():
    #text = input('prompt>')
    text = """
    BEGIN
        BEGIN
            a := 5;
            b := a - 2;
        END;
        x := 11;
    END.
    """
    lexer = Lexer(text)
    parser = Parser(lexer)
    interpreter = Interpreter(parser)
    interpreter.izvrsi()
    print(interpreter.GLOBAL)
    #prikazLKD(interpreter.stablo)



if __name__ == '__main__':
    main()