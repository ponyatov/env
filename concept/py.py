
import sys

log = open('log.log', 'w')

class Sym:
    tag = 'sym'
    def __init__(self, V): self.val = V ; self.nest = []
    def __iadd__(self, o): self.nest.append(o) ; return self
    def head(self): return '<%s:%s> @%s' % (self.tag, self.val, id(self))
    def dump(self, depth=0):
        S = '\n' + '\t' * depth + self.head()
        for i in self.nest: S += i.dump(depth+1)
        return S
    def __repr__(self): return self.dump()

class Op(Sym):
    tag = 'op'

import ply.lex  as lex
import ply.yacc as yacc

tokens = ['SYM', 'COLON']

t_ignore = ' \t\r\n'
t_ignore_comment = '\#.*'

def t_COLON(t):
    ':'
    t.value = Op(t.value) ; return t
def t_SYM(t):
    r'[a-zA-Z0-9_]+'
    t.value = Sym(t.value) ; return t

def p_REPL_empty(p): ' REPL : '
def p_REPL_recur(p):
    r' REPL : REPL ex '
    print >> log, p[2]
def p_ex_SYM(p):
    ' ex : SYM '
    p[0] = p[1]
def p_inher(p):
    ' ex : ex COLON ex '
    p[0] = p[2] ; p[0] += p[1] ; p[0] += p[3] 

def t_error(t): print 'lexer/error', t
def p_error(p): print 'parse/error', p

lex.lex()
yacc.yacc(debug=False, write_tables=False).parse(
    open('src.src').read()
#     sys.stdin.read()
    )
