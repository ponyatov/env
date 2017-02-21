class Sym:
    tag = 'sym'
    def __init__(self, V): self.val = V ; self.nest = [] ; self.attr = {}
    def __iadd__(self, o): self.nest.append(o); return self
    def head(self): return '<%s:%s> @%x' % (self.tag, self.val, id(self))
    def __repr__(self): return self.dump()
    def dump(self, depth=0):
        S = '\n' + '\t' * depth + self.head()
        for i in self.attr:
            S += '\n%s%s = %s' % ('\t'*(depth+1), i, self.attr[i].head())
        for j in self.nest:
            S += j.dump(depth + 1)
        return S
    def eval(self,E):
        if self.val in E.attr: return E.attr[self.val]
        for i in range(len(self.nest)): self.nest[i] = self.nest[i].eval(E)
        return self
    def add(self,o): raise BaseException('%s + %s'%(self.head(),o.head()))
    def sub(self,o): raise BaseException('%s - %s'%(self.head(),o.head()))

class Env(Sym): tag = 'env'
glob = Env('global')

class Int(Sym):
    tag = 'int'
    def __init__(self, V): Sym.__init__(self, V) ; self.val = int(self.val)
    def add(self, o):
        if o.tag == 'int': return Int(self.val + o.val)
        Sym.add(self, o)
    def sub(self, o):
        if o.tag == 'int': return Int(self.val - o.val)
        Sym.sub(self, o)
glob.attr['n']=Int(111)

class Vector(Sym):
    tag = 'vector'
    def __init__(self): Sym.__init__(self, '[]')

class Op(Sym):
    tag = 'op'
    def __init__(self, V): Sym.__init__(self, V)
    def eval(self,E):
        if self.val == '~':    return self.nest[0]
        else:                Sym.eval(self, E)
        if len(self.nest) == 2:
            if self.val == '-': return self.nest[0].sub(self.nest[1])
        return self

class Fn(Sym):
    tag = 'fn'
    def __init__(self,V): Sym.__init__(self, V)

