%{
#include "core/hpp.hpp"
%}
%option noyywrap yylineno
%%
^.end					{yyterminate();}	// .end directive (stop procesing)

\(						TOC(Op,LP)			// brackets
\)						TOC(Op,RP)
\[						TOC(Op,LQ)
\]						TOC(Op,RQ)
\{						TOC(Op,LC)
\}						TOC(Op,RC)

\=						TOC(Op,EQ)			// operators

[a-zA-Z0-9_]+			TOC(Sym,SYM)		// symbol
[ \t\r\n]+				{}					// drop spaces
.						{yyerror("lexer");}	// undef char
