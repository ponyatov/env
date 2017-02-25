#ifndef _H_HPP
#define _H_HPP

#include <iostream>
#include <cstdlib>
#include <cmath>
#include <cassert>
using namespace std;

extern int yylineno;
extern char* yytext;
typedef void* yyscan_t;
extern int yyparse();
extern void yyerror(string);
#include "ypp.tab.hpp"
extern int yylex(YYSTYPE*,YYLTYPE*);

#endif // _H_HPP
