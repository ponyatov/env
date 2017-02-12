#include "hpp.hpp"

Env* glob = new Env("global");
Env::Env(string V):Sym("env",V){}
void glob_init() {}
