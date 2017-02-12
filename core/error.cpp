#include "hpp.hpp"
Error::Error(string V):Sym("error",V) { yyerror(V); }
Error::Error(Sym*o):Error(o->dump()){}
