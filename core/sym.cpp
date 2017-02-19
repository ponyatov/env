#include "core/hpp.hpp"

Sym::Sym(string T, string V) { tag = T; val = V; }
Sym::Sym(string V):Sym("sym",V){}

Sym* Sym::push(Sym*o) { nest.push_back(o); return this; }

string Sym::head() { ostringstream os;
	os <<"<"<< tag <<":"<< val <<"> @"<<this ; return os.str(); }
string Sym::pad(int n) { string S; for (int i=0;i<n;i++) S += '\t'; return S; }
unordered_set<Sym*>dump_recur;
string Sym::dump(int depth) { string S = "\n"+pad(depth)+head();
	// block infty dump
	if (depth==0) dump_recur.clear();
	if (dump_recur.find(this)!=dump_recur.end())
		return S+"\n"+pad(depth+1)+"...";
	dump_recur.insert(this);
	// ////
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

//Sym* Sym::pfxadd() { return new Error(" + "+head()); }
//Sym* Sym::pfxsub() { return new Error(" - "+head()); }
//
//Sym* Sym::add(Sym*o) { return new Error(head()+" + "+o->head()); }
//Sym* Sym::sub(Sym*o) { return new Error(head()+" - "+o->head()); }
//Sym* Sym::mul(Sym*o) { return new Error(head()+" * "+o->head()); }
//Sym* Sym::div(Sym*o) { return new Error(head()+" / "+o->head()); }
//Sym* Sym::pow(Sym*o) { return new Error(head()+" ^ "+o->head()); }
//
//Sym* Sym::ass(Sym*o) {
//	if (tag==o->tag && val==o->val) return ok(o); else return fail(o);
//}
//
//Sym* Sym::ok(Sym*o) { return (new Sym("test:ok"))->push(this)->push(o); }
//Sym* Sym::fail(Sym*o) {
//	return new Error( (new Sym("test:fail"))->push(this)->push(o) ); }
