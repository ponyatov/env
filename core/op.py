from sym import *
class Op(Sym):
    tag = 'op'
    def eval(self, E):
        Sym.eval(self, E)
        if len(self.nest) == 1:
            if self.val == '+': return self.nest[0].pfxadd()
            if self.val == '-': return self.nest[0].pfxsub()
        if len(self.nest) == 2:
            if self.val == '+': return self.nest[0].add(self.nest[1])
            if self.val == '-': return self.nest[0].sub(self.nest[1])
            if self.val == '*': return self.nest[0].mul(self.nest[1])
            if self.val == '/': return self.nest[0].div(self.nest[1])
            if self.val == '^': return self.nest[0].pow(self.nest[1])
            if self.val == '?=': return self.nest[0].ass(self.nest[1])
        raise BaseException(self.dump())
