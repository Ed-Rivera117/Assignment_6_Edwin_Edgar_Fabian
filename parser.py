import ply.yacc as yacc
from pip._vendor.distlib.compat import raw_input
from lex import tokens


def p_rules(p):
    ''' exp : exp PLUS term
                | exp MINUS term
        term : term TIMES factor
                | term DIVIDE factor '''

    if p[2] == '+':
        p[0] = p[1] + p[3]
    elif p[2] == '-':
        p[0] = p[1] - p[3]
    elif p[2] == '*':
        p[0] = p[1] * p[3]
    elif p[2] == '/':
        p[0] = p[1] / p[3]


def p_term_factor(p):
    'term : factor'
    p[0] = p[1]


def p_factor_num(p):
    'factor : NUMBER'
    p[0] = p[1]


def p_factor_exp(p):
    'factor : LP exp RP'
    p[0] = p[2]


def p_error(p):
    print("Syntax error input")


#Build
parser = yacc.yacc()

# while True:
#     try:
#         s = raw_input('PL > ')
#     except EOFError:
#         break
#     if not s: continue
#     result = parser.parse(s)
#     print(result)