class Sym:
    def __init__(self, T, V):
        self.tag = T; self.val = V;
        self.nest = []; self.attr = {}
    def __repr__(self): return self.dump()
    def head(self):
        return '<%s:%s> @%s' % (self.tag, self.val, id(self))
    def dump(self, depth=0, header=''):
        S = '\n' + '\t' * depth + header + self.head()
        for i in self.attr: S += self.attr[i].dump(depth+1,'%s = '%i)
        for j in self.nest: S += j.dump(depth+1)
        return S
    def __mod__(self, o):   self.attr[o.val] = o; return o
    def __iadd__(self,o):   self.nest.append(o); return self
    def eval(self): return self
    def pfxadd(self): return Error()
    
class Error(Sym):
    def __init__(self,V): 

class Int(Sym):
    def __init__(self,V):
        Sym.__init__(self, 'int', V) ; self.val = int(self.val)
class Num(Sym):
    def __init__(self,V):
        Sym.__init__(self, 'num', V) ; self.val = float(self.val)
        
class Op(Sym):
    def __init__(self,V): Sym.__init__(self, 'op', V)
    def eval(self):
        if len(self.nest) == 1:
            if self.val == '+': return self.nest[0].pfxadd()
            if self.val == '-': return self.nest[0].pfxsub()
        return self