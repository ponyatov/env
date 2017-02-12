#include "hpp.hpp"
#define YYERR "\n\n"<<yylineno<<":"<<msg<<"["<<yytext<<"]\n\n"
void yyerror(string msg) { cout<<YYERR; cerr<<YYERR; exit(-1); }
int main() { glob_init(); return yyparse(); }

Sym::Sym(string T, string V) { tag = T; val = V; }
Sym::Sym(string V):Sym("sym",V){}

Sym* Sym::push(Sym*o) { nest.push_back(o); return this; }

string Sym::head() { ostringstream os;
	os <<"<"<< tag <<":"<< val <<"> @"<<this ; return os.str(); }
string Sym::pad(int n) { string S; for (int i=0;i<n;i++) S += '\t'; return S; }
string Sym::dump(int depth) { string S = "\n"+pad(depth)+head();
	for (auto it=nest.begin(),e=nest.end();it!=e;it++)
		S += (*it)->dump(depth+1);
	return S; }

Int::Int(string V):Sym("int","") { val = atoi(V.c_str()); }
string Int::head() { ostringstream os;
	os <<"<"<< tag <<":"<< val <<"> @"<<this ; return os.str(); }

Num::Num(string V):Sym("num","") { val = atof(V.c_str()); }
string Num::head() { ostringstream os;
	os <<"<"<< tag <<":"<< val <<"> @"<<this ; return os.str(); }

Op::Op(string V):Sym("op",V){}

Env* glob = new Env("global");
Env::Env(string V):Sym("env",V){}
void glob_init() {}
