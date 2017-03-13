import os,sys
import ply.lex  as lex
import ply.yacc as yacc

from sym import *

tokens = ['SYM','INT','NUM','LC','RC','COLON','ADD','SUB']

t_ignore = ' \t\r'
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
t_ignore_comment = '\#.*'

def t_LC(t):
    '{'
    t.value = Op(t.value) ; return t
def t_RC(t):
    '}'
    t.value = Op(t.value) ; return t
def t_COLON(t):
    ':'
    t.value = Op(t.value) ; return t

def t_ADD(t):
    '\+'
    t.value = Op(t.value) ; return t
def t_SUB(t):
    '\-'
    t.value = Op(t.value) ; return t

def t_NUM(t):
    ' ([0-9]+)?\.[0-9]* '    
    t.value = Num(t.value) ; return t
def t_INT(t):
    ' [0-9]+ '    
    t.value = Int(t.value) ; return t
def t_SYM(t):
    ' [a-zA-Z0-9_\.]+ '
    t.value = Sym('sym',t.value) ; return t
    
precedence = (
    ('left','ADD','SUB'),
    ('left','PFX'),
    )    
    
def p_REPL_none(p): ' REPL : '
def p_REPL_recur(p):
    ' REPL : REPL ex '
    print p[2]
    print '-'*20
    print p[2].eval()
    print '='*40
    
def p_ex_SYM(p):
    ' ex : SYM \n| INT \n| NUM '
    p[0] = p[1]
    
def p_ex_pfx_ADD(p):
    ' ex : ADD ex %prec PFX '
    p[0] = p[1] ; p[0] += p[2]
def p_ex_pfx_SUB(p):
    ' ex : SUB ex %prec PFX '
    p[0] = p[1] ; p[0] += p[2]

def p_ex_lambda(p):
    ' ex : LC lambda RC '
    p[0] = p[2]
def p_lambda(p):
    ' lambda : '
    p[0] = Sym('lambda','')
def p_lambda_par(p):
    ' lambda : lambda SYM COLON '
    p[0] = p[1] ; p[0] % p[2]
def p_lambda_ex(p):
    ' lambda : lambda ex '
    p[0] = p[1] ; p[0] += p[2]
    
def t_error(t): print 'lexer/error',t
def p_error(p): print 'parse/error',p

lex.lex()
yacc.yacc(debug=False,write_tables=False).parse(sys.stdin.read())
