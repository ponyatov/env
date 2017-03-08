# # import operator as op
 
from parsimonious.grammar import Grammar
# from __builtin__ import str

class Mini:
     
    def parse(self, source):
        grammar = '\n'.join(j.__doc__
            for i, j in self.__class__.__dict__.items()
            if not i.startswith('__') and j.__doc__)
        print grammar
        return Grammar(grammar)['program'].parse(source)

    def eval(self, source):
        node = self.parse(source) if isinstance(source, str) else source
        method = getattr(self, node.expr_name, lambda *a:'error')
        return method(node, [self.eval(n) for n in node])
    
    def program(self, node, children):
        ' program = number * '
        return children
    
    def number(self, node, children):
        ' number = ~"[0-9]+" ~"\s*" '
        return int(node.text)
 
def test_hello():
    assert True
 
def test_class():
    assert Mini() != Mini()

def test_empty():
    assert Mini().eval('') == [] 
    
def test_numbers():
    assert Mini().eval('42') == [42]
    assert Mini().eval('42 12') == [42 , 12]
