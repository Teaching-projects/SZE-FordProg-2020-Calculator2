from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def _add_tokens(self):
        self.lexer.add('NUMBER', r'[0-9]+')
        self.lexer.add('TYPE', r'__[a-z]+')
        self.lexer.add('IDENTIFIER', r'[a-zA-Z][a-zA-Z0-9_-]*')
        self.lexer.add('EQUAL', r'=')
        self.lexer.add('SEMICOLON', r';')
        self.lexer.add('ADDITION', r'\+')
        self.lexer.add('SUBTRACTION', r'\-')
        self.lexer.add('MULTIPLICATION', r'\*')
        self.lexer.add('DIVISION', r'/')
        self.lexer.add('MODULO', r'%')
        self.lexer.ignore('\s+')

    def get_lexer(self):
        self._add_tokens()
        return self.lexer.build()
