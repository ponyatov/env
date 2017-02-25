#ifndef _H_HPP
#define _H_HPP

#include <iostream>
#include <cstdlib>
#include <cmath>
#include <cassert>
using namespace std;

extern int yylineno;
extern char* yytext;
#include "ypp.tab.hpp"
typedef void* yyscan_t;
extern int yylex(YYSTYPE*,YYLTYPE*);
extern void yyerror(YYLTYPE*,yyscan_t,string);
extern int yyparse(yyscan_t);

#endif // _H_HPP
