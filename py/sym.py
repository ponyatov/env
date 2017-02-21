class Sym:
	def __init__(self,T,V): self.tag=T ; self.val=V ; self.nest=[] ; self.attr={}
	def __iadd__(self,o): self.nest.append(o) ; return self
	def __repr__(self): return self.dump()
	def head(self): return '%s:%s #%x'%(self.tag,self.val,id(self))
	def dump(self,depth=0):
		'full internals dump'
		S = '\n%s%s'%('\t'*depth,self.head())
		for i in self.attr:
			S += '\n%s%s = '%('\t'*(depth+1),i) + self.attr[i].dump(depth+2)
		for j in self.nest: S += j.dump(depth+1)
		return S
	def deep(self): return max(len(self.attr),len(self.nest))
	def revhead(self):
		if self.tag==self.__class__.__name__.lower(): customtag=''
		else: customtag='%s:'%self.tag
		return '%s%s'%(customtag,self.val)
	def rev(self,depth=0):
		'reverse source'
		if self.deep(): pad='\n%s'%('\t'*depth)
		else: pad=''
		S = '%s%s'%(pad,self.revhead())
		for i in self.attr:
			S += '\n%s%% %s'%('\t'*(depth+1),i)
			if i <> self.attr[i].val:
				S += ' = %s'%self.attr[i].rev(depth+2)
		for j in self.nest:
			S += '\n%s/ %s'%('\t'*(depth+1),j.rev(depth+1))
		return S
class Num(Sym):
	def __init__(self,V):
		Sym.__init__(self,'num',V) ; self.val = float(self.val)
class Vector(Sym):
	def __init__(self): Sym.__init__(self,'vector','[]')
	def head(self): return '%s #%x'%(self.val,id(self))
	def rev(self,depth):
		S = '[ '
		for i in self.nest: S += '%s '%i.rev(depth+1)
		return S+']'
class Op(Sym):
	def __init__(self,V): Sym.__init__(self,'op',V)

