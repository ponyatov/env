#ifndef _H_YACC
#define _H_YACC

extern int yyparse();			// parse input    			\ parser interface
extern void yyerror(string);	// error callback
#include "tmp/bI.parser.hpp"	// tokens defs for lexer	/

#endif // _H_YACC
