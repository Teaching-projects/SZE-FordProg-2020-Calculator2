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
    return t
    
lexer = lex.lex()

precedence = (
    ('left', 'ADDITION', 'SUBTRACTION'),
    ('left', 'MULTIPLICATION', 'DIVISION')
)

def p_calc(p):
    '''
    calc : expression
         | var_init
         | var_declare
         | var_assign
         | conditional_statement
         | empty
    '''
    
def p_var_declare(p):
    '''
    var_declare : TYPE NAME SEMICOLON
    '''
    global env
    
    env[p[2]] = 0
    print(f"Variable '{p[2]}' has been created.")
    
def p_var_init(p):
    '''
    var_init : TYPE NAME EQUALS expression SEMICOLON
    '''    
    global env
    
    if p[1] == 'integer':
        env[p[2]] = int(p[4])
    else:
        env[p[2]] = p[4]

    print(f"Variable '{p[2]}' has a value as '{env[p[2]]}'")
            
def p_var_assign(p):
    '''
    var_assign : NAME EQUALS expression SEMICOLON
    '''
    global env
    
    if exists(p[1]):
        env[p[1]] = p[3]
#        print(f"Variable '{p[1]}' has a new value as '{env[p[1]]}'")
    
def p_conditional_statement(p):
    '''
    conditional_statement : KEYWORD_IF OPEN_PARENTHESES condition CLOSE_PARENTHESES OPEN_BRACES var_assign CLOSE_BRACES KEYWORD_ELSE OPEN_BRACES var_assign CLOSE_BRACES
    '''
    
    if p[3]:
        p[6]
    else:
        p[10]
    
def p_condition(p):
    '''
    condition : bool_expression LESS_SIGN bool_expression
              | bool_expression GREATER_SIGN bool_expression 
    '''
    
    if exists(p[1]):
        p[0] = eval(str(env[p[1]]) + p[2] + str(p[3]))
        
    
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
               | expression DIVISION expression
               | expression ADDITION expression
               | expression SUBTRACTION expression
    '''
    
    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]
        
    print(p[0])

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
    
    p[0] = p[1]
    if exists(p[1]):
        print(env[p[1]])
    
def p_error(p):
    print("Syntax error found!")

def p_empty(p):
    '''
    empty :
    '''

def exists(variable):
    if variable not in env:
        print(f"{variable} is an undeclared variable!")
        return False
    else:
        return True
    
parser = yacc.yacc()

env = {}
while True:
    try:
        s = input('>>')
    except EOFError:
        break
    parser.parse(s)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
    
