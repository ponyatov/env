import ply.lex  as lex
import ply.yacc as yacc
from sym import *

tokens = [ 'SYM','NUM' ,'DIV','MOD','EQ','COLON', 'LP','RP','LQ','RQ']

t_ignore = ' \t\r'
t_ignore_comment = '\#.*'
def t_newline(t):
	r'\n'
	t.lexer.lineno += 1

def t_LP(t):
	r'\('
	t.value = Op(t.value) ; return t
def t_RP(t):
	r'\)'
	t.value = Op(t.value) ; return t
def t_LQ(t):
	r'\['
	t.value = Op(t.value) ; return t
def t_RQ(t):
	r'\]'
	t.value = Op(t.value) ; return t

def t_DIV(t):
	r'\/'
	t.value = Op(t.value) ; return t
def t_MOD(t):
	r'\%'
	t.value = Op(t.value) ; return t
def t_EQ(t):
	r'\='
	t.value = Op(t.value) ; return t
def t_COLON(t):
	r'\:'
	t.value = Op(t.value) ; return t

def t_NUM(t):
	r'[0-9]+(\.[0-9]*)?([eE][\+\-]?[0-9]+)?'
	t.value = Num(t.value) ; return t
def t_SYM(t):
	r'[a-zA-Z0-9_]+'
	t.value = Sym('sym',t.value) ; return t

precedence = (('left','DIV','MOD'),('right','EQ'),('nonassoc','COLON'),)

def p_REPL_none(p): ' REPL : '
def p_REPL_recur(p):
	' REPL : REPL ex '
	print p[2].dump()
	print '-'*20
	print p[2].rev()
	print '='*40
def p_ex_sym(p):
	''' ex : SYM
			| NUM'''
	p[0]=p[1]
def p_ex_parens(p):
	r' ex : LP ex RP '
	p[0]=p[2]
def p_ex_colon(p):
	' ex : ex COLON ex '
	p[0] = Sym(p[1].val,p[3].val)

def p_ex_div(p):
	' ex : ex DIV ex '
	p[0] = p[1] ; p[0] += p[3]
def p_ex_eq(p):
	' ex : ex MOD ex EQ ex '
	p[0] = p[1] ; p[0].attr[p[3].val]=p[5]
def p_ex_mod(p):
	' ex : ex MOD ex '
	p[0] = p[1] ; p[0].attr[p[3].val]=p[3]

def p_ex_vector(p):
	' ex : LQ vector RQ '
	p[0]=p[2]
def p_vector_none(p):
	' vector : '
	p[0] = Vector()
def p_vector_ex(p):
	' vector : vector ex '
	p[0] = p[1] ; p[0] += p[2]

def t_error(t): print 'lexer/error',t
def p_error(p): print 'parse/error',p

lex.lex()
parser = yacc.yacc(debug=False,write_tables=False)

