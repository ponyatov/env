#ifndef _H_HPP
#define _H_HPP

#include <iostream>
#include <cstdlib>
#include <cmath>
#include <cassert>
using namespace std;

#include "ypp.tab.hpp"
typedef void* yyscan_t;
extern yyscan_t scanner;
extern int yylex_init(yyscan_t* scanner);
extern int yylex_destroy(yyscan_t yyscanner);
extern int yylex(YYSTYPE*,yyscan_t);
extern int yyget_lineno(yyscan_t);
extern char* yyget_text(yyscan_t);
extern int yyparse(yyscan_t);
extern void yyerror(yyscan_t,string);

#endif // _H_HPP
