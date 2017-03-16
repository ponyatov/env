############## class tree ##############

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
