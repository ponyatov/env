#ifndef _H_HPP
#define _H_HPP

#include <iostream>
#include <limits>
#include <sstream>
#include <cstdlib>
#include <cmath>
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
	map<string,Sym*> attr;		// \ attributes
	Sym* lookup(string);		// /
	virtual string dump(int=0);	// \ dump in tree form
	virtual string head();		// <T:V> header
	string pad(int);			// / left pad tree element
	virtual Sym* eval(Sym*E);	// evaluate/compute object
	virtual Sym* pfxadd();		// + A
	virtual Sym* pfxsub();		// - A
	virtual Sym* add(Sym*);		// A + B
	virtual Sym* sub(Sym*);		// A - B
	virtual Sym* mul(Sym*);		// A * B
	virtual Sym* div(Sym*);		// A / B
	virtual Sym* pow(Sym*);		// A ^ B
};

struct Env:Sym { Env(string); };			// \ environment
extern Env *glob;							// <env:global>
extern void glob_init();					// / init

struct Error:Sym { Error(string); };		// error

struct Int:Sym {
	Int(string); Int(long); long val;		// integer
	string head(); Sym*eval(Sym*);
	Sym* pfxadd(); Sym* pfxsub();
	Sym* add(Sym*); Sym* sub(Sym*);
	Sym* mul(Sym*); Sym* div(Sym*);
	Sym* pow(Sym*);
	};
struct Num:Sym {							// floating number
	Num(string); Num(double); double val;
	string head(); Sym*eval(Sym*);
	Sym* pfxadd(); Sym* pfxsub();
	Sym* add(Sym*); Sym* sub(Sym*);
	Sym* mul(Sym*); Sym* div(Sym*);
	Sym* pow(Sym*);
	};

struct Op:Sym { Op(string);		// operator
	Sym*eval(Sym*); };

extern int yylex();				// get next token \ lexer interface
extern int yylineno;			// token line
extern char* yytext;			// current lexeme
								// new token      /
#define TOC(C,X) { \
	yylval.o = new C(yytext); return X; }
//glob->attr[yytext] = yylval.o;

extern int yyparse();			// parse input    \ parser interface
extern void yyerror(string);	// error callback /
#include "ypp.tab.hpp"			// tokens definition

#endif // _H_HPP
