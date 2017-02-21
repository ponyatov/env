import sys ; sys.stdout = open(sys.argv[0]+'.log','w')

import ply.lex  as lex
import ply.yacc as yacc

class Sym:
	tag = 'sym'
	def __init__(self, V): self.val = V ; self.nest = [] ; self.attr = {}
	def __iadd__(self, o): self.nest.append(o); return self
	def head(self): return '<%s:%s>' % (self.tag, self.val)
	def __repr__(self): return self.dump()
	def dump(self, depth=0):
		S = '\n' + '\t' * depth + self.head()
		for i in self.attr: S += ',%s=%s' % (i, self.attr[i].head())
		for j in self.nest: S += j.dump(depth + 1)
		return S
	def eval(self,E):
		if self.val in E.attr: return E.attr[self.val]
		for i in range(len(self.nest)): self.nest[i] = self.nest[i].eval(E)
		return self
class Env(Sym): tag = 'env'
glob = Env('global')
class Int(Sym):
	tag = 'int'
	def __init__(self, V): Sym.__init__(self, V) ; self.val = int(self.val)
glob.attr['n']=Int(111)
class Vector(Sym):
	tag = 'vector'
	def __init__(self): Sym.__init__(self, '[]')
class Op(Sym):
	tag = 'op'
	def __init__(self, V): Sym.__init__(self, V)
	def eval(self,E):
		if self.val == '~':	return self.nest[0]
		else:				Sym.eval(self, E)
		return self
class Fn(Sym):
	tag = 'fn'
	def __init__(self,V): Sym.__init__(self, V)

tokens = [ 'SYM' , 'INT', 
		'LP', 'RP' , 'LQ', 'RQ', 'LC', 'RC' , 'LS', 'GR' ,
		'EQ', 'COMMA',
		'ADD', 'SUB', 'POW',
		'IF', 'ELSE' ]

t_ignore = ' \t\r'
t_ignore_comment = '\#.*'
def t_newline(t):
	r'\n'
	t.lexer.lineno += 1
def t_INT(t):
	r'[0-9]+'
	t.value = Int(t.value) ; return t
def t_IF(t):
	r'if'
	t.value = Op(t.value) ; return t
def t_ELSE(t):
	r'else'
	t.value = Op(t.value) ; return t
def t_SYM(t):
	r'[a-zA-Z0-9_]+'
	t.value = Sym(t.value) ; return t
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
def t_LC(t):
	r'\{'
	t.value = Op(t.value) ; return t
def t_RC(t):
	r'\}'
	t.value = Op(t.value) ; return t
def t_LS(t):
	r'\<'
	t.value = Op(t.value) ; return t
def t_GR(t):
	r'\>'
	t.value = Op(t.value) ; return t
def t_EQ(t):
	r'\='
	t.value = Op(t.value) ; return t
def t_COMMA(t):
	r'\,'
	t.value = Op(t.value) ; return t
def t_ADD(t):
	r'\+'
	t.value = Op(t.value) ; return t
def t_SUB(t):
	r'\-'
	t.value = Op(t.value) ; return t
def t_POW(t):
	r'\^'
	t.value = Op(t.value) ; return t

def p_REPL_none(p):	' REPL : '
def p_REPL_recur(p):
	' REPL : REPL ex '
	print p[2]
	print '-'*20
	print p[2].eval(glob)
	print '-'*20
	print glob
	print '='*40
def p_ex_SYM(p):
	' ex : SYM '
	p[0] = p[1]
def p_ex_NUM(p):
	' ex : INT '
	p[0] = p[1]
def p_fn_def(p):
	' ex : SYM SYM LP params RP LC vector RC '
	p[0] = Fn(p[2].val) ; p[0].attr['ret'] = p[1]
	for i in p[4].nest: p[0].attr[i.val] = i 
	for j in p[7].nest: p[0] += j
def p_fn_use(p):
	' ex : SYM LP params RP'
	p[0] = Op('@') ; p[0] += p[1]
	for i in p[3].nest: p[0] += i
def p_params_comma(p):
	' params : params COMMA ex '
	p[0] = p[1] ; p[0] += p[3]
def p_params_single(p):
	' params : ex '
	p[0] = Vector() ; p[0] += p[1]	
def p_params_none(p):
	' params : '
	p[0] = Vector()
def p_ex_parens(p):
	' ex : LP ex RP '
	p[0] = p[2]
def p_ex_less(p):
	' ex : ex LS ex '
	p[0] = p[2] ; p[0] += p[1] ; p[0] += p[3]
def p_ex_lesseq(p):
	' ex : ex LS EQ ex '
	p[0] = Op('<=') ; p[0] += p[1] ; p[0] += p[4]
def p_ex_great(p):
	' ex : ex GR ex '
	p[0] = p[2] ; p[0] += p[1] ; p[0] += p[3]
def p_ex_eq(p):
	' ex : ex EQ ex '
	p[0] = p[2] ; p[0] += p[1] ; p[0] += p[3]
def p_ex_add(p):
	' ex : ex ADD ex '
	p[0] = p[2] ; p[0] += p[1] ; p[0] += p[3]
def p_ex_sub(p):
	' ex : ex SUB ex '
	p[0] = p[2] ; p[0] += p[1] ; p[0] += p[3]
def p_ex_vector(p):
	' ex : LQ vector RQ '
	p[0] = p[2]
def p_vector_none(p):
	' vector : '
	p[0] = Vector()
def p_vector_ex(p):
	' vector : vector ex '
	p[0] = p[1] ; p[0] += p[2]
def p_ret(p):
	' ex : POW params '
	p[0] = p[1]
	for i in p[2].nest : p[0] += i
def p_ex_else(p):
	' ex : IF ex ex  ELSE ex'
	p[0] = p[1] ; p[0] += p[2] ; p[0] += p[3] ; p[0] += p[5]
def p_ex_if(p):
	' ex : IF ex ex '
	p[0] = p[1] ; p[0] += p[2] ; p[0] += p[3]
	
	
def t_error(t): print 'lexer/error', t
def p_error(p): print 'parse/error', p

lex.lex()
yacc.yacc(debug=False, write_tables=False).parse('''
n-1
# def fib(n) {
# 	if n<=0 ^0
# 	if n<2 ^1
# 	else ^ fib(n-1)+fib(n-2)
# }
# 
# def none(){}
# 
# def main() {
# #none()
# #print fib(11)
# }
''')

