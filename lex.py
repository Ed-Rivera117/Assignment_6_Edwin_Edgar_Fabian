import ply.lex as lex

tokens = ['NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LP', 'RP', 'LB', 'RB', 'ID', 'EQUALS', 'LESSEQUAL',
          'GREATEREQUAL']

reserved = {
    'if': 'IF', 'then': 'THEN', 'else': 'ELSE', 'while': 'WHILE', 'createsockect': 'CREATESOCKET',
    'bindsocket':'BINDSOCKET', 'receiverepeated':'RECEIVEREPEATED', 'connectlocalclient':'CONNECTLOCALCLIENT',
    'repeatedmessages':'REPEATEDMESSAGES', 'finishlocalclient':'FINISHLOCALCLIENT',
    'bindexternalserversocket':'BINDEXTERNALSERVERSOCKET', 'multtimesreceive':'MULTTIMESSAGESRECEIVE',
    'closeexternalserver':'CLOSEEXTERNALSERVER', 'bindexternalclientsocket':'BINDEXTERNALCLIENTSOCKET',
    'multtimesmessagessent':'MULTTIMESSAGESSENT', 'closeexternalclient':'CLOSEEXTERNALCLIENT'
}

tokens += list(reserved.values())

# Regular expressions
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LP = r'\('
t_RP = r'\)'
t_LB = r'\['
t_RB = r'\]'
t_EQUALS = r'\='
t_LESSEQUAL = r'<='
t_GREATEREQUAL = r'>='


def t_ID(tk):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    tk.type = reserved.get(tk.value, 'ID')  # Check reserved values
    return tk


def t_NUMBER(tk):
    r'\d+'
    tk.value = int(tk.value)
    return tk


def t_Newline(tk):
    r'\n+'
    tk.lexer.lineno += len(tk.value)


t_ignore = ' \t'


def t_error(tk):
    print('Illegal Character')
    tk.lexer.skip(1)
