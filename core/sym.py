
class Sym:
    tag = 'sym'
    def __init__(self, V): self.val = V ; self.nest = [] ; self.attr = {}
    def __iadd__(self, o): return self.push(o)
    def push(self, o): self.nest.append(o); return self
    def __repr__(self): return self.dump()
    def head(self): return '<%s:%s> @%s' % (self.tag, self.val, id(self))
    def dump(self, depth=0):
        S = '\n' + '\t' * depth + self.head()
        for i in self.nest: S += i.dump(depth + 1)
        return S
    def eval(self,E):
        for i in range(len(self.nest)): self.nest[i] = self.nest[i].eval(E)
        return self
    def pfxadd(self): raise BaseException('+ %s' % self.head())
    def pfxsub(self): raise BaseException('- %s' % self.head())
    def add(self, o): raise BaseException(self.head() + ' + ' + o.head())
    def sub(self, o): raise BaseException(self.head() + ' - ' + o.head())
    def mul(self, o): raise BaseException(self.head() + ' * ' + o.head())
    def div(self, o): raise BaseException(self.head() + ' / ' + o.head())
    def pow(self, o): raise BaseException(self.head() + ' ^ ' + o.head())

class Env(Sym): tag = 'env'
glob = Env('global')
