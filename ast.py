

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

class Broj(Node):
    """
    Cvor koji predstavlja jedan broj.
    """
    def __init__(self,token):
        self.token = token
