import sys

class Sym:
    tag = 'sym'
    def __init__(self, V): self.val = V ; self.nest = [] ; self.attr = {}
    def __iadd__(self, o): self.nest.append(o); return self
    def head(self): return '<%s:%s> @%x' % (self.tag, self.val, id(self))
    def __repr__(self): return self.dump()
    dump_reg=[]
    def dump(self, depth=0):
#         if depth==0: self.dump_reg=[]
#         if self in self.dump_reg: return '\n%s...'%('\t'*depth)
#         else: self.dump_reg.append(self)
        S = '\n' + '\t' * depth + self.head()
        for i in self.attr:
            S += '\n%s%s = %s' % ('\t'*(depth+1), i, self.attr[i].head())
        for j in self.nest:
            S += j.dump(depth + 1)
        return S
    def lookup(self, V):
        print >>sys.stderr,'lookup',V,'in',self.head()
        if V in self.attr: return self.attr[V]
#         if V == self.val: return self
#         if V in self.attr: return self.attr[V]
#         if V == self.val: return self
        return None
    def eval(self,E):
        L = E.lookup(self.val)
        if L: return L
        for i in range(len(self.nest)): self.nest[i] = self.nest[i].eval(E)
        return self
    def add(self,o): raise BaseException('%s + %s'%(self.head(),o.head()))
    def sub(self,o): raise BaseException('%s - %s'%(self.head(),o.head()))

class Env(Sym): tag = 'env'
glob = Env('global')

class Arg(Sym): tag = 'arg'

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

