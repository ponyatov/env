#ifndef _H_HPP
#define _H_HPP

#include <iostream>
#include <sstream>
#include <cstdlib>
#include <vector>
#include <map>
using namespace std;

struct Sym {
	string val;									// value
	string doc;									// docstring
	Sym(string);								// token constructor
	vector<Sym*> nest; Sym* push(Sym*);			// nest[]ed elements = vector
	map<string,Sym*> env; Sym* attr(Sym*,Sym*);	// attr{}ibutes = environment
	virtual string dump(int=0,string head="");	// homoiconic dump
	string pad(int);
};

extern int yylex();
extern int yylineno;
extern char* yytext;
#define TOC(C,X) { yylval.o = new C(yytext); return X; }
extern int yyparse();
extern void yyerror(string);
#include "ypp.tab.hpp"

#endif // _H_HPP
