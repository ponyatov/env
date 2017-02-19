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
\@						TOC(Op,AT)
\<						TOC(Op,LESS)
\>						TOC(Op,GREAT)

"skype://"					TOC(Op,SKYPE)		// skype
([a-z0-9_]+\.)+[a-z0-9]+	TOC(Domain,DOMAIN)	// domain

[a-zA-Z0-9_]+			TOC(Sym,SYM)		// symbol
[ \t\r\n]+				{}					// drop spaces
.						{yyerror("lexer");}	// undef char
	