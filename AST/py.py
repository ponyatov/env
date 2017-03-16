import os, sys

# class tree

class AST:
    tag = ''
    def __init__(self, V): self.val = V ; self.nest = [] ; self.attr = {}
    def __iadd__(self, o): self.nest.append(o) ; return self
    def __repr__(self): return self.dump()
    def head(self): return '<%s:%s> @%s' % (self.tag, self.val, id(self))
    def dump(self, depth=0):
        S = '\n' + '\t' * depth + self.head()
        for i in self.nest: S += i.dump(depth+1)
        return S
class Int(AST):
    tag = 'int'
    def __init__(self,V): AST.__init__(self, V) ; self.val = int(V)
class Num(AST):
    tag = 'num'
    def __init__(self,V): AST.__init__(self, V) ; self.val = float(V)
class Sym(AST): tag = 'sym'
class Op(AST): tag = 'op'

# parser 
import ply.lex  as lex
import ply.yacc as yacc

tokens = ['SYM','INT','NUM',
          'LP','RP',
          'ADD','SUB','MUL','DIV','POW']

t_ignore = ' \t\r'
t_ignore_comment = '\#.*'
def t_newline(t):
    r'\n'
    t.lexer.lineno += 1

def t_LP(t):
    '\('
    t.value = Op(t.value) ; return t
def t_RP(t):
    '\)'
    t.value = Op(t.value) ; return t

def t_ADD(t):
    '\+'
    t.value = Op(t.value) ; return t
def t_SUB(t):
    '\-'
    t.value = Op(t.value) ; return t
def t_MUL(t):
    '\*'
    t.value = Op(t.value) ; return t
def t_DIV(t):
    '\/'
    t.value = Op(t.value) ; return t
def t_POW(t):
    '\^'
    t.value = Op(t.value) ; return t

def t_NUM(t):
    '([0-9]+(\.[0-9]*)?|\.[0-9]+)([eE][\+\-]?[0-9]+)?'
    t.value = Num(t.value) ; return t
def t_INT(t):
    '[0-9]+'
    t.value = Int(t.value) ; return t
def t_SYM(t):
    '[a-zA-Z0-9_]+'
    t.value = Sym(t.value) ; return t

precedence = (
    ('left','ADD','SUB'),
    ('left','MUL','DIV'),
    ('right','POW'),
    ('left','PFX'),
    )

def p_REPL_none(p): ' REPL : '
def p_REPL_ex(p):
    ' REPL : REPL ex '
    print p[2]
    
def p_ex_SYM(p):
    ' ex : SYM '
    p[0] = p[1]
def p_ex_INT(p):
    ' ex : INT '
    p[0] = p[1]
def p_ex_NUM(p):
    ' ex : NUM '
    p[0] = p[1]
def p_ex_PARENS(p):
    ' ex : LP ex RP '
    p[0] = p[2]

def p_ex_PLUS(p):
    ' ex : ADD ex %prec PFX '
    p[0] = p[1] ; p[0] += p[2]
def p_ex_MUNIS(p):
    ' ex : SUB ex %prec PFX '
    p[0] = p[1] ; p[0] += p[2]
def p_ex_ADD(p):
    ' ex : ex ADD ex '
    p[0] = p[2] ; p[0] += p[1] ; p[0] += p[3]
def p_ex_SUB(p):
    ' ex : ex SUB ex '
    p[0] = p[2] ; p[0] += p[1] ; p[0] += p[3]
def p_ex_MUL(p):
    ' ex : ex MUL ex '
    p[0] = p[2] ; p[0] += p[1] ; p[0] += p[3]
def p_ex_DIV(p):
    ' ex : ex DIV ex '
    p[0] = p[2] ; p[0] += p[1] ; p[0] += p[3]
def p_ex_POW(p):
    ' ex : ex POW ex '
    p[0] = p[2] ; p[0] += p[1] ; p[0] += p[3]

def t_error(t): print 'lexer/error',t
def p_error(p): print 'parse/error',p

lex.lex()
yacc.yacc(debug=False,write_tables=False).parse(sys.stdin.read())
