#include "hpp.hpp"

Num::Num(string V):Sym("num","") { val = atof(V.c_str()); }
Num::Num(double D):Sym("num","") { val = D; }
Sym* Num::eval(Sym*E) { return this; }
string Num::head() { ostringstream os;
	os.precision(numeric_limits<double>::digits10 + 1);
	os <<"<"<< tag <<":"<< val <<"> @"<<this ; return os.str(); }
Sym* Num::pfxadd() { return this; }
Sym* Num::pfxsub() { return new Num(-val); }

Sym* Num::add(Sym*o) {
	if (o->tag=="int") return new Num(val + /**/ dynamic_cast<Int*>(o)->val);
	if (o->tag=="num") return new Num(val + /**/ dynamic_cast<Num*>(o)->val);
	return Sym::add(o);
}

Sym* Num::sub(Sym*o) {
	if (o->tag=="int") return new Num(val - /**/ dynamic_cast<Int*>(o)->val);
	if (o->tag=="num") return new Num(val - /**/ dynamic_cast<Num*>(o)->val);
	return Sym::sub(o);
}

Sym* Num::mul(Sym*o) {
	if (o->tag=="int") return new Num(val * /**/ dynamic_cast<Int*>(o)->val);
	if (o->tag=="num") return new Num(val * /**/ dynamic_cast<Num*>(o)->val);
	return Sym::mul(o);
}

Sym* Num::div(Sym*o) {
	if (o->tag=="int") return new Num(val / /**/ dynamic_cast<Int*>(o)->val);
	if (o->tag=="num") return new Num(val / /**/ dynamic_cast<Num*>(o)->val);
	return Sym::div(o);
}

Sym* Num::pow(Sym*o) {
	if (o->tag=="int") return new Num(std::pow(val,dynamic_cast<Int*>(o)->val));
	if (o->tag=="num") return new Num(std::pow(val,dynamic_cast<Num*>(o)->val));
	return Sym::pow(o);
}

Sym* Num::ass(Sym*o) {
	if (tag==o->tag && abs(val - dynamic_cast<Num*>(o)->val)<1e-9) return ok(o);
	else return fail(o); }
