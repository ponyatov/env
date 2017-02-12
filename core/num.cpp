#include "hpp.hpp"

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
