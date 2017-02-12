from sym import *
class Num(Sym):
    tag = 'num'
    def __init__(self, V): Sym.__init__(self, V) ; self.val = float(V)
    def pfxadd(self): return self
    def pfxsub(self): return Num(-self.val)
    def add(self, o):
        if o.tag in ['int','num']: return Num(self.val + o.val)
        return Sym.add(self, o)
    def sub(self, o):
        if o.tag in ['int','num']: return Num(self.val - o.val)
        return Sym.sub(self, o)
    def mul(self, o):
        if o.tag in ['int','num']: return Num(self.val * o.val)
        return Sym.mul(self, o)
    def div(self, o):
        if o.tag in ['int','num']: return Num(self.val / o.val)
        return Sym.div(self, o)
    def pow(self, o):
        if o.tag in ['int','num']: return Num(self.val ** o.val)
        return Sym.pow(self, o)
