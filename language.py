from lexer import Lexer

text_input = """
    __int x = 5;
    x = 1 + 2 * 3;
    """

lexer = Lexer().get_lexer()
tokens = lexer.lex(text_input)

for token in tokens:
    print(token)
