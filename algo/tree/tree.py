import os,sys
sys.stdout = open('tree.log','w')
dot = open('tree.dot','w')
print >>dot,'digraph { node [shape=record];'

class T:
    def __init__(self, V):
        self.val = V ; self.nest = [] ; self.attr = {}
    def __repr__(self): return self.dump()
    def head(self): return '%s @%s'%(self.val,id(self))
    def dump(self, depth=0):
        S = '\n%s%s'%('\t'*depth,self.head())
        for i in self.attr:
            S += '\n%s%s = %s' % ('\t'*(depth+1),i,self.attr[i].dump(depth + 2))
        for j in self.nest:
            S += j.dump(depth + 1)
        return S
    def __div__(self, o): self.nest.append(o) ; return self
    def __mod__(self, o): self.attr[o.val] = o; return self
    def dot(self):
        S = '_%s[label="%s|{'%(id(self),self.val)
        for i in self.attr: S += '<%s>%s|'%(i,i)
        S = S[:-1]+'}'
        for j in self.nest: S += '|%s'%j.val
        S += '"];\n'
        for i in self.attr:
            S += self.attr[i].dot()
            S += '_%s -> _%s [label="%s",color=red];\n'%(id(self),id(self.attr[i]),i)
        for j in self.nest:
#             S += j.dot()
            S += '_%s -> _%s [label="%s",color=blue];\n'%(id(self),id(j),j.val)
        return S

import ply.lex  as lex
import ply.yacc as yacc

tokens = [ 'T' , 'M','D' ]

t_ignore = ' \t\r\n'
t_ignore_comment = '\#.*'
def t_M(t):
    r'\%'
    t.value = T(t.value) ; return t
def t_D(t):
    r'\/'
    t.value = T(t.value) ; return t
def t_T(t):
    r'[a-zA-Z0-9_]+'
    t.value = T(t.value) ; return t
    
precedence = (('left','M','D'),)
    
def p_REPL_none(p): ' REPL : '
def p_REPL_recur(p):
    ' REPL : REPL ex '
    print p[2]
    print >>dot,p[2].dot()
def p_ex(p):
    ' ex : T '
    p[0] = p[1]
def p_ex_m(p):
    ' ex : ex M ex '
    p[0] = p[1] ; p[0] % p[3]
def p_ex_d(p):
    ' ex : ex D ex '
    p[0] = p[1] ; p[0] / p[3]

def t_error(t): print 'lexer/error',t
def p_error(p): print 'parse/error',p

lex.lex()
yacc.yacc(write_tables=False,debug=False).parse('''
a % b / a
''')

print >>dot,'}'
dot.close()
os.system('dot -Tpdf -o tree.pdf tree.dot')
