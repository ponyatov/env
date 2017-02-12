#include "hpp.hpp"
#define YYERR "\n\n"<<yylineno<<": "<<msg<<" ["<<yytext<<"]\n\n"
void yyerror(string msg) { cout<<YYERR; cerr<<YYERR; exit(-1); }
int main() { glob_init(); return yyparse(); }

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

Error::Error(string V):Sym("error",V) { yyerror(V); }

Sym* Sym::pfxadd() { return new Error(" + "+head()); }
Sym* Sym::pfxsub() { return new Error(" - "+head()); }

Sym* Sym::add(Sym*o) { return new Error(head()+" + "+o->head()); }
Sym* Sym::sub(Sym*o) { return new Error(head()+" - "+o->head()); }
Sym* Sym::mul(Sym*o) { return new Error(head()+" * "+o->head()); }
Sym* Sym::div(Sym*o) { return new Error(head()+" / "+o->head()); }
Sym* Sym::pow(Sym*o) { return new Error(head()+" ^ "+o->head()); }

Int::Int(string V):Sym("int","") { val = atoi(V.c_str()); }
Int::Int(long N):Sym("int","") { val = N; }
Sym* Int::eval(Sym*E) { return this; }
string Int::head() { ostringstream os;
	os.precision(numeric_limits<long>::digits10 + 1);
	os <<"<"<< tag <<":"<< val <<"> @"<<this ; return os.str(); }
Sym* Int::pfxadd() { return this; }
Sym* Int::pfxsub() { return new Int(-val); }

Sym* Int::add(Sym*o) {
	if (o->tag=="int") return new Int(val + /**/ dynamic_cast<Int*>(o)->val);
	if (o->tag=="num") return new Num(val + /**/ dynamic_cast<Num*>(o)->val);
	return Sym::add(o);
}

Sym* Int::sub(Sym*o) {
	if (o->tag=="int") return new Int(val - /**/ dynamic_cast<Int*>(o)->val);
	if (o->tag=="num") return new Num(val - /**/ dynamic_cast<Num*>(o)->val);
	return Sym::add(o);
}

Sym* Int::mul(Sym*o) {
	if (o->tag=="int") return new Int(val * /**/ dynamic_cast<Int*>(o)->val);
	if (o->tag=="num") return new Num(val * /**/ dynamic_cast<Num*>(o)->val);
	return Sym::add(o);
}

Sym* Int::div(Sym*o) {
	if (o->tag=="int") return new Int(val / /**/ dynamic_cast<Int*>(o)->val);
	if (o->tag=="num") return new Num(val / /**/ dynamic_cast<Num*>(o)->val);
	return Sym::add(o);
}

Sym* Int::pow(Sym*o) { // A^B
	if (o->tag=="int") { // int:B
		if (dynamic_cast<Int*>(o)->val <0) // B<0
			return new Num(std::pow(val,dynamic_cast<Int*>(o)->val));
		long r = 1; for (int i=0;i<dynamic_cast<Int*>(o)->val;i++) r *= val;
		return new Int(r);
	}
	if (o->tag=="num") return new Num(std::pow(val,dynamic_cast<Num*>(o)->val));
	return Sym::add(o);
}

Num::Num(string V):Sym("num","") { val = atof(V.c_str()); }
Num::Num(double D):Sym("num","") { val = D; }
Sym* Num::eval(Sym*E) { return this; }
string Num::head() { ostringstream os;
	os.precision(numeric_limits<double>::digits10 + 1);
	os <<"<"<< tag <<":"<< val <<"> @"<<this ; return os.str(); }
Sym* Num::pfxadd() { return this; }
Sym* Num::pfxsub() { return new Num(-val); }

Sym* Num::mul(Sym*o) {
	if (o->tag!=tag) return Sym::mul(o);
	return new Num(val * /**/ dynamic_cast<Num*>(o)->val);
}

Op::Op(string V):Sym("op",V){}
Sym* Op::eval(Sym*E) {
	if (val!="~") Sym::eval(E); else return nest[0];
	switch (nest.size()) {
		case 1:
			if (val=="+") return nest[0]->pfxadd();
			if (val=="-") return nest[0]->pfxsub();
		case 2:
			if (val=="+") return nest[0]->add(nest[1]);
			if (val=="-") return nest[0]->sub(nest[1]);
			if (val=="*") return nest[0]->mul(nest[1]);
			if (val=="/") return nest[0]->div(nest[1]);
			if (val=="^") return nest[0]->pow(nest[1]);
	}
	return this; }

Env* glob = new Env("global");
Env::Env(string V):Sym("env",V){}
void glob_init() {}
