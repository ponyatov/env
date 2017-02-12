#ifndef _H_HPP
#define _H_HPP

#include <iostream>
#include <sstream>
#include <cstdlib>
#include <vector>
#include <map>
using namespace std;

struct Sym {
	string tag;					// type/class tag
	string val;					// value: any data can be represented in text
	Sym(string T,string V);		// <T:V> \ constructors
	Sym(string V);				// token /
	vector<Sym*> nest;			// \ nest[]ed elements
	Sym* push(Sym*);			// /
	virtual string dump(int=0);	// \ dump in tree form
	virtual string head();		// <T:V> header
	string pad(int);			// / left pad tree element
};

struct Env:Sym { Env(string); };	// \ environment
extern Env *glob;					// <env:global>
extern void glob_init();			// / init

struct Int:Sym { Int(string); long val;		// integer
	string head(); };
struct Num:Sym { Num(string); double val;	// floating number
	string head(); };

struct Op:Sym { Op(string); };	// operator

extern int yylex();				// get next token \ lexer interface
extern int yylineno;			// token line
extern char* yytext;			// current lexeme /
#define TOC(C,X) { yylval.o = new C(yytext); return X; } /* new token */
extern int yyparse();			// parse input    \ parser interface
extern void yyerror(string);	// error callback /
#include "ypp.tab.hpp"			// tokens definition

#endif // _H_HPP
