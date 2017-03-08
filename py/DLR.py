# # import operator as op
 
from parsimonious.grammar import Grammar
from __builtin__ import str

# print Grammar(\n')['program'].parse('42')
 
class Mini:
     
#     def __init__(self, env={}): self.env = env
#     
    def parse(self, source):
#         # select grammar definition using __doc__strings introspection
        grammar = '\n'.join(j.__doc__
            for i, j in self.__class__.__dict__.items()
            if not i.startswith('__') and j.__doc__)
        print grammar
        return Grammar(grammar)['program'].parse(source)

    def eval(self, source):
        node = self.parse(source) if isinstance(source, str) else source
        method = getattr(self, node.expr_name)
        return method(node, [self.eval(n) for n in node])
     
    def program(self, node, children):
        r' program = ~"[0-9]+" '
        return int(node.text)
 
def test_hello():
    assert True
 
def test_class():
    assert Mini() != Mini()
    
def test_numbers():
    assert Mini().eval('42') == 42
