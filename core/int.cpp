#include "hpp.hpp"

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
