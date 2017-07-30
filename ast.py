

class Node(object):
    """
    Bazna klasa cvora ast-a
    koju svi cvorovi nasledjuju.
    """
    pass

class BinarnaOperacija(Node):
    """
    Cvor koji predstavlja binarnu operaciju.
    Sadrzi pokazivace na dva operanda i token operacije.
    """
    def __init__(self,levo,operacija,desno):
        self.levo = levo
        self.operacija = operacija
        self.desno = desno

    def __str__(self):
        return '{}'.format(self.operacija)


class UnarnaOperacija(Node):
    """
    Cvor koji predstavlja unarnu operaciju.
    Sadrzi token operacije(PLUS | MINUS) i pokazivac na izraz (sledeci cvor u ast).
    """
    def __init__(self,operacija,izraz):
        self.operacija = operacija
        self.izraz = izraz

    def __str__(self):
        return '{}'.format(self.operacija)


class Broj(Node):
    """
    Cvor koji predstavlja jedan broj.
    """
    def __init__(self,token):
        self.token = token

    def __str__(self):
        return '{}'.format(self.token)


class Var(Node):
    """
    Cvor predstavlja promenljivu.
    """
    def __init__(self,token):
        self.token = token
        self.vrednost = token.vrednost

class Compound(Node):
    """
    Cvor predstavlja jedan BEGIN-END blok.
    Niz deca sadrzi adrese statement-a tog bloka.
    """
    def __init__(self):
        self.deca = []

class Assign(Node):
    """
    Cvor predstavlja operaciju dodele vrednosti.
    Operacija predstavlja token dodele.
    """
    def __init__(self,levo,operacija,desno):
        self.levo = levo
        self.token = operacija
        self.desno = desno

class NoOp(Node):
    """
    Cvor koji odgovara empty pravilu gramatike.
    Zbog toga sto je i 'BEGIN END.' validan program.
    """
    pass