from sym import *

import ply.lex  as lex
import ply.yacc as yacc

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

def p_REPL_none(p):    ' REPL : '
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
    p[0] = Fn(p[2].val) ; p[0].attr['type'] = p[1]
    for i in p[4].nest: p[0].attr[i.val] = Arg(i.val) 
    for j in p[7].nest: p[0] += j
    glob.attr[p[0].val] = p[0]      # reg function
    p[0].eval(p[0])                 # link variables by selflookup
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
parser = yacc.yacc(debug=False, write_tables=False)
