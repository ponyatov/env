#include "core/hpp.hpp"
Login::Login(string V):Sym("login",V) {
	attr["name"]=new Str(V);
	attr["password"]=new Str(""); }
