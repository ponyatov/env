import sys

from sym import *
from int import *
from num import *
from op import *

import ply.lex  as lex
import ply.yacc as yacc

tokens = [ 'SYM' , 'INT', 'NUM', 'EOL',
          'ADD', 'SUB', 'MUL', 'DIV', 'POW'
          ]

t_ignore = ' \t\r'
t_ignore_coment = '\#.*'
def t_EOL(t):
    r'\n'
    t.lexer.lineno += 1
    t.value = Op('EOL') ; return t

def t_ADD(t):
    r'\+'
    t.value = Op(t.value) ; return t
def t_SUB(t):
    r'\-'
    t.value = Op(t.value) ; return t
def t_MUL(t):
    r'\*'
    t.value = Op(t.value) ; return t
def t_DIV(t):
    r'\/'
    t.value = Op(t.value) ; return t
def t_POW(t):
    r'\^'
    t.value = Op(t.value) ; return t

def t_NUM(t):
    r'([0-9]+(\.[0-9]*([eE][\+\-]?[0-9]+)?|[eE][\+\-]?[0-9]+)|\.[0-9]+)'
    t.value = Num(t.value) ; return t
def t_INT(t):
    r'[0-9]+'
    t.value = Int(t.value) ; return t
    
precedence = [
    ('left','ADD','SUB'),
    ('left','MUL','DIV'),
    ('left','POW'),
    ('right','PFX'),
    ]
    
def p_REPL_none(p): ' REPL : '
def p_REPL_eol(p):  ' REPL : REPL EOL '
def p_REPL(p):
    ' REPL : REPL ex '
    print p[2]
    print '-' * 20,
    print p[2].eval(glob).dump()
    print '-' * 20,
    print glob
    print '=' * 40

def p_ex_scalar(p):
    ' ex : scalar '
    p[0] = p[1]
def p_scalar(p):
    ''' scalar : SYM
            | INT
            | NUM '''
    p[0] = p[1]
    
def p_ex_pfxadd(p):
    ' ex : ADD ex %prec PFX '
    p[0] = p[1] ; p[0] += p[2]
def p_ex_pfxsub(p):
    ' ex : SUB ex %prec PFX '
    p[0] = p[1] ; p[0] += p[2]
    
def p_ex_add(p):
    ' ex : ex ADD ex '
    p[0] = p[2] ; p[0] += p[1] ; p[0] += p[3]
def p_ex_sub(p):
    ' ex : ex SUB ex '
    p[0] = p[2] ; p[0] += p[1] ; p[0] += p[3]
def p_ex_mul(p):
    ' ex : ex MUL ex '
    p[0] = p[2] ; p[0] += p[1] ; p[0] += p[3]
def p_ex_div(p):
    ' ex : ex DIV ex '
    p[0] = p[2] ; p[0] += p[1] ; p[0] += p[3]
def p_ex_pow(p):
    ' ex : ex POW ex '
    p[0] = p[2] ; p[0] += p[1] ; p[0] += p[3]

def t_error(t): raise BaseException('lexer/error %s' % t)
def p_error(p): raise BaseException('parse/error %s' % p)

lex.lex()
yacc.yacc(debug=False, write_tables=False).parse(sys.stdin.read())
