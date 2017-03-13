#ifndef _H_HPP
#define _H_HPP

#include <iostream>
#include <sstream>
#include <cstdlib>
#include <vector>
#include <map>
using namespace std;

struct Sym {
	string tag,val;
	Sym(string,string); Sym(string);
	vector<Sym*> nest; void push(Sym*); void clear();
	virtual string head();
	string pad(int);
	virtual string dump(int=0);
};

struct Int:Sym { Int(string); long val; string head(); };
struct Num:Sym { Num(string); double val; string head(); };

struct Fn:Sym { Fn(string); };

extern int yylex();
extern int yylineno;
extern char* yytext;
#define TOC(C,X) { yylval.o = new C(yytext); return X; }
extern int yyparse();
extern void yyerror(string);
#include "ypp.tab.hpp"

// FORTH machine

extern Sym stack;

#endif // _H_HPP
