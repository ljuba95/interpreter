class Parser(object):

    def __init__(self,lexer):
        self.lexer = lexer
        self.trenutni_token = self.lexer.next_token() #inicijalizacija prvog tokena

    def parse(self):
        pass