#include "hpp.hpp"

Sym::Sym(string T, string V) { tag = T; val = V; }
Sym::Sym(string V):Sym("sym",V){}

Sym* Sym::push(Sym*o) { nest.push_back(o); return this; }

string Sym::head() { ostringstream os;
	os <<"<"<< tag <<":"<< val <<"> @"<<this ; return os.str(); }
string Sym::pad(int n) { string S; for (int i=0;i<n;i++) S += '\t'; return S; }
string Sym::dump(int depth) { string S = "\n"+pad(depth)+head();
	for (auto it=attr.begin(),e=attr.end();it!=e;it++)
		S += "\n"+pad(depth+1) + it->first + " =" + it->second->dump(depth+2);
	for (auto it=nest.begin(),e=nest.end();it!=e;it++)
		S += (*it)->dump(depth+1);
	return S; }

Sym* Sym::lookup(string V) {
	if (attr.find(V)==attr.end()) return NULL; else return attr[V]; }

Sym* Sym::eval(Sym*E) {
	Sym*L = E->lookup(val); if (L) return L;			// env{} lookup
	for (auto it=nest.begin(),e=nest.end();it!=e;it++)	// recursive eval
		(*it) = (*it)->eval(E);
	return this; }

Sym* Sym::pfxadd() { return new Error(" + "+head()); }
Sym* Sym::pfxsub() { return new Error(" - "+head()); }

Sym* Sym::add(Sym*o) { return new Error(head()+" + "+o->head()); }
Sym* Sym::sub(Sym*o) { return new Error(head()+" - "+o->head()); }
Sym* Sym::mul(Sym*o) { return new Error(head()+" * "+o->head()); }
Sym* Sym::div(Sym*o) { return new Error(head()+" / "+o->head()); }
Sym* Sym::pow(Sym*o) { return new Error(head()+" ^ "+o->head()); }
