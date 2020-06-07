import ply.lex as lex
import ply.yacc as yacc
import sys

tokens = [
    'INTEGER',
    'FLOAT',
    'NAME',
    'ADDITION',
    'SUBTRACTION',
    'MULTIPLICATION',
    'DIVISION',
    'EQUALS',
    'TYPE',
    'SEMICOLON',
    'KEYWORD_IF',
    'KEYWORD_ELSE',
    'OPEN_PARENTHESES',
    'CLOSE_PARENTHESES',
    'OPEN_BRACES',
    'CLOSE_BRACES',
    'LESS_SIGN',
    'GREATER_SIGN',
]

t_ADDITION = r'\+'
t_SUBTRACTION = r'\-'
t_MULTIPLICATION = r'\*'
t_DIVISION = r'\/'
t_EQUALS = r'\='
t_SEMICOLON = r'\;'
t_OPEN_PARENTHESES = r'\('
t_CLOSE_PARENTHESES = r'\)'
t_OPEN_BRACES = r'\{'
t_CLOSE_BRACES = r'\}'
t_LESS_SIGN = r'<'
t_GREATER_SIGN = r'>'

t_ignore = r' '

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_INTEGER(t):
    r'\d+'
    t.value = int(t.value)
    return t
    
def t_TYPE(t):
    r'integer|float'
    t.type = 'TYPE'
    return t
    
def t_KEYWORD_IF(t):
    r'if'
    t.type = 'KEYWORD_IF'
    return t
    
def t_KEYWORD_ELSE(t):
    r'else'
    t.type = 'KEYWORD_ELSE'
    return t
    
def t_NAME(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = 'NAME'
    return t

def t_error(t):
    print("Illegal character!")
    t.lexer.skip(1)
    
lexer = lex.lex()

precedence = (
    ('left', 'ADDITION', 'SUBTRACTION'),
    ('left', 'MULTIPLICATION', 'DIVISION')
)

def p_calc(p):
    '''
    calc : expression
         | var_init
         | var_definition
         | var_assign
         | conditional_statement
         | empty
    '''
    print(run(p[1]))
    
def p_var_init(p):
    '''
    var_init : TYPE NAME SEMICOLON
    '''
    p[0] = ('declaration', p[1], p[2], 0)
    
def p_var_definition(p):
    '''
    var_definition : TYPE NAME EQUALS expression SEMICOLON
    '''
    p[0] = ('declaration', p[1], p[2], p[4])
            
def p_var_assign(p):
    '''
    var_assign : NAME EQUALS expression SEMICOLON
    '''
    p[0] = ('assignment', p[1], p[3])
    
def p_conditional_statement(p):
    '''
    conditional_statement : KEYWORD_IF OPEN_PARENTHESES condition CLOSE_PARENTHESES OPEN_BRACES var_assign CLOSE_BRACES KEYWORD_ELSE OPEN_BRACES var_assign CLOSE_BRACES
    '''
    p[0] = ('conditional_statement', p[3], p[6], p[10])
    
def p_condition(p):
    '''
    condition : bool_expression LESS_SIGN bool_expression
              | bool_expression GREATER_SIGN bool_expression 
    '''
    p[0] = (p[2], p[1], p[3])
    
def p_bool_expression(p):
    '''
    bool_expression : INTEGER
                    | FLOAT
                    | NAME
    '''
    p[0] = p[1]
    
def p_expression(p):
    '''
    expression : expression MULTIPLICATION expression
    expression : expression DIVISION expression
    expression : expression ADDITION expression
    expression : expression SUBTRACTION expression
    '''
    p[0] = (p[2], p[1], p[3])    

def p_expression_integer_float(p):
    '''
    expression : INTEGER
               | FLOAT
    '''
    p[0] = p[1]
    
def p_expression_integer_var(p):
    '''
    expression : NAME
    '''
    p[0] = ('var', p[1])
    
def p_error(p):
    print("Syntax error found!")

def p_empty(p):
    '''
    empty :
    '''
    p[0] = None
    
parser = yacc.yacc()
env = {}

def run(p):
    global env
    if type(p) == tuple:
        if p[0] == '+':
            return run(p[1]) + run(p[2])
        elif p[0] == '-':
            return run(p[1]) - run(p[2])
        elif p[0] == '*':
            return run(p[1]) * run(p[2])
        elif p[0] == '/':
            return run(p[1]) / run(p[2])
        elif p[0] == 'declaration':
            if p[1] == 'integer':
                env[p[2]] = run(int(p[3]))
            else:
                env[p[2]] = run(p[3])
        elif p[0] == '=':
            env[p[1]] = run(p[2])
        elif p[0] == 'assignment':
            if p[1] not in env:
                return f"{p[1]} is an undeclared variable!"
            else:
                env[p[1]] = run(p[2])
        elif p[0] == 'conditional_statement':
            for element in p:
                if type(element) == tuple:
                    if element[1] not in env:
                        return f"{element[1]} is an undeclared variable!"
            if p[1][0] == '>':
                if env[p[1][1]] > p[1][2]:
                    run(p[2])
                else:
                    run(p[3])
            else:
                if env[p[1][1]] < p[1][2]:
                    run(p[2])
                else:
                    run(p[3])
        elif p[0] == 'var':
            if p[1] not in env:
                return "Undeclared variable found!"
            else:
                return env[p[1]]
    else:
        return p
        
while True:
    try:
        s = input('>>')
    except EOFError:
        break
    parser.parse(s)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
