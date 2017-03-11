
import sys

log = open('log.log','w')

import ply.lex  as lex
import ply.yacc as yacc

tokens = ['SYM']

t_ignore = ' \t\r\n'
def t_SYM(t):
    r'.'
    return t

def p_REPL_empty(p): ' REPL : '
def p_REPL_recur(p):
    r' REPL : REPL SYM '
    print >>log,p[2]

def t_error(t): print 'lexer/error',t
def p_error(p): print 'parse/error',p

lex.lex()
yacc.yacc(debug=False,write_tables=False).parse(
    open('src.src').read()
#     sys.stdin.read()
    )