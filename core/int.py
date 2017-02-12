from sym import *
from num import *
class Int(Sym):
    tag = 'int'
    def __init__(self, V): Sym.__init__(self, V) ; self.val = int(V)
    def pfxadd(self): return self
    def pfxsub(self): return Int(-self.val)
    def add(self, o):
        if o.tag == 'int': return Int(self.val + o.val)
        if o.tag == 'num': return Num(self.val + o.val)
        return Sym.add(self, o)
    def sub(self, o):
        if o.tag == 'int': return Int(self.val - o.val)
        if o.tag == 'num': return Num(self.val - o.val)
        return Sym.add(self, o)
    def mul(self, o):
        if o.tag == 'int': return Int(self.val * o.val)
        if o.tag == 'num': return Num(self.val * o.val)
        return Sym.mul(self, o)
    def div(self, o):
        if o.tag == 'int': return Int(self.val / o.val)
        if o.tag == 'num': return Num(self.val / o.val)
        return Sym.mul(self, o)
    def pow(self, o):
        if o.tag == 'int':
            if o.val >= 0:  return Int(self.val ** o.val)
            else:           return Num(self.val ** o.val)
        if o.tag == 'num':  return Num(self.val ** o.val)
        return Sym.pow(self, o)
