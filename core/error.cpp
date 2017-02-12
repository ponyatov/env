#include "hpp.hpp"
Error::Error(string V):Sym("error",V) { yyerror(V); }
