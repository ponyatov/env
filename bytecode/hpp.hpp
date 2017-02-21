#ifndef _H_HPP
#define _H_HPP

#include <iostream>
#include <sstream>
#include <iomanip>
#include <cassert>
#include <vector>
using namespace std;

struct Sym {
	string tag; string val; Sym(string,string); Sym(string);
	virtual string dump();
	virtual void reloc(Sym*); };
struct Int:Sym { int val; Int(string); virtual string dump(); };

struct Saver:Sym { Saver(string); string dump(); };

struct Cmd0:Sym { Cmd0(string V,int OP);
	int addr; int op; string dump() override; };
struct Cmd1:Cmd0 { Cmd1(string V,int OP,int W);
	int addr; int op; int w; string dump() override; };

struct Nop:Cmd0 { Nop(string V); };
struct Halt:Cmd0 { Halt(string V); };

struct Jmp:Cmd1 { Jmp(string V); void reloc(Sym*); };

extern int yylex();
extern int yylineno;
extern char* yytext;
#define TOC(C,X) { yylval.o = new C(yytext); return X; }
extern int yyparse();
extern void yyerror(string);
#include "ypp.tab.hpp"

#define Dsz 0x10
extern int Dp;
extern Sym* D[Dsz];
#define Rsz 0x100
extern int Rp;
extern int R[Rsz];
#define Msz 0x1000
extern int Ip;
extern int Mp;
extern int M[Msz];
extern int VM(int,char**);

#endif // _H_HPP

