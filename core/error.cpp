#include "core/hpp.hpp"

// yacc error callback
#define YYERR "\n\n"<<yylineno<<": "<<msg<<" ["<<yytext<<"]\n\n"
void yyerror(string msg) { cout<<YYERR; cerr<<YYERR; exit(-1); }

Error::Error(string V):Sym("error",V) { yyerror(V); }
//Error::Error(Sym*o):Error(o->dump()){}
