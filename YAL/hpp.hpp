#ifndef _H_HPP
#define _H_HPP

#include <iostream>
#include <cstdlib>
using namespace std;

extern int yylex();
extern int yylineno;
extern char* yytext;
extern int yyparse();
extern void yyerror(string);
#include "ypp.tab.hpp"

#endif // _H_HPP
