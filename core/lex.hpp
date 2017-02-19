#ifndef _H_LEX
#define _H_LEX

extern int yylex();				// get next token \ lexer interface
extern int yylineno;			// token line
extern char* yytext;			// current lexeme
								// new token      /
#define TOC(C,X) { yylval.o = new C(yytext); return X; }

#endif // _H_LEX
