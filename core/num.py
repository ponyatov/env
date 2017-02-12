from sym import *
class Num(Sym):
    tag = 'num'
    def __init__(self, V): Sym.__init__(self, V) ; self.val = float(V)
    def pfxadd(self): return self
    def pfxsub(self): return Num(-self.val)
    def mul(self, o):
        if o.tag in ['int','num']: return Num(self.val * o.val)
        return Sym.add(self, o)
