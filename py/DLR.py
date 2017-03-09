from parsimonious.grammar import Grammar
import operator

class Mini:
    
    def __init__(self, env={}):
        self.env = env
        self.env['sum'] = lambda *args: sum(args)
     
    def parse(self, source):
        grammar = '\n'.join(j.__doc__
            for i, j in self.__class__.__dict__.items()
            if not i.startswith('__') and j.__doc__)
#         print grammar
        return Grammar(grammar)['program'].parse(source)

    def eval(self, source):
        node = self.parse(source) if isinstance(source, str) else source
        method = getattr(self, node.expr_name, lambda *a:'error')
        return method(node, [self.eval(n) for n in node])
    
    def program(self, node, children):
        ' program = expr * '
        return children
    
    def expr(self, node, children):
        ' expr = call / infix / assign / number / name  '
        return children[0]
    
    def call(self, node, children):
        ' call = name "(" _ args _ ")" '
        name, _, _, args, _, _ = children
        return name(*args)
        
    def args(self, node, children):
        ' args = expr* '
        return children
    
    def infix(self, node, children):
        ' infix = "(" _ expr _ op _ expr _ ")" '
        _, _, expr1, _, op, _, expr2, _, _ = children
        return op(expr1, expr2)
        
    def op(self, node, children):
        ' op = ~"[\+\-\*\/]" '
        return {
            '+':operator.add, '-':operator.sub,
            '*':operator.mul, '/':operator.div
            }[node.text]
    
    def assign(self, node, children):
        ' assign = lvalue "=" _ expr '
        lvalue, _, _, expr = children
        self.env[lvalue] = expr ; return expr
    
    def lvalue(self, node, children):
        ' lvalue = ~"[a-z]+" _ '
        return node.text.strip()
    
    def name(self, node, children):
        ' name = ~"[a-z]+" _ '
        return self.env[node.text.strip()]
    
    def number(self, node, children):
        ' number = ~"[0-9]+" _ '
        return int(node.text)
    
    def _(self, node, children):
        ' _ = ~"\s*" '
 
def test_hello():
    assert True
 
def test_class():
    assert Mini() != Mini()

def test_empty():
    assert Mini().eval('') == []
    
def test_numbers():
    assert Mini().eval('42') == [42]
    assert Mini().eval('42 12') == [42 , 12]

def test_vars():
    assert Mini(env={'a':42}).eval('a ') == [42]
    assert Mini().eval('a=2 \n a') == [2, 2]

def test_ops():
    assert Mini().eval('(42 +2)') == [44] 
    assert Mini().eval('(42 +(2*4))') == [50] 

def test_funcall():
    assert Mini().eval('sum(10 20)') == [30] 
    assert Mini().eval('sum(10 20 30)') == [60] 
    assert Mini().eval('sum()') == [0] 
