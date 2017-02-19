#include "core/hpp.hpp"

Env* env = new Env("global");
Env::Env(string V):Sym("env",V){}
void env_init() {
	env->attr["A"] = new Sym("A");
	env->attr["env"] = env;
	env->attr["Z"] = new Sym("Z");
}
