#include "core/hpp.hpp"
#line 3 "core/env.cpp"

Env* env = new Env("global");
Env::Env(string V):Sym("env",V){}
void env_init() {
	env->attr["env"] = env;
	env->attr["meta"]= new Env("meta");
	// meta
	env->attr["meta"]->attr["MODULE"]	= new Str(MODULE);
	env->attr["meta"]->attr["TITLE"]	= new Str(TITLE);
	env->attr["meta"]->attr["ABOUT"]	= new Str(ABOUT);
	env->attr["meta"]->attr["AUTHOR"]	= new Str(AUTHOR);
	env->attr["meta"]->attr["LICENSE"]	= new Str(LICENSE);
	env->attr["meta"]->attr["GITHUB"]	= new Str(GITHUB);
	env->attr["meta"]->attr["LOGO"]		= new Str(LOGO);
}
Sym* Env::div(Sym*o) {
	Sym* L = lookup(o->val) ; if (L) return L;
	attr[o->val]=new Env(o->val); return attr[o->val];
}
