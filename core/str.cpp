#include "core/hpp.hpp"
Str::Str(string V):Sym("str",V){}
string Str::head() { ostringstream os;
	os <<"'"<< val <<"' @"<<this ; return os.str(); }
