#ifndef _H_HPP
#define _H_HPP

#ifdef JIT
#include "libtcc.h"		// Use Fabrice Bellard's Tiny C Compiler as backend
#endif

#include <iostream>
#include <cstdlib>
#include <cassert>
using namespace std;

extern int yylex();
extern int yylineno;
extern char* yytext;
extern int yyparse();
extern void yyerror(string);
#include "ypp.tab.hpp"

#endif // _H_HPP
