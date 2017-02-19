%{
#include "core/hpp.hpp"
%}
%defines %union { Sym*o; }
%token <o> SYM					/* scalars: symbol			*/
%token <o> EQ					/* operators: =				*/
%token <o> LP RP LQ RQ LC RC	/* brackets: () [] {}		*/
%type <o> ex scalar	vector		/* expression scalar vector	*/
%%
REPL : | REPL ex	{ cout << $2->dump() << endl; }

ex : scalar
scalar : SYM

ex : LP ex RP		{ $$=$2; }
ex : ex EQ ex		{ $$=$2; $$->push($1); $$->push($3); }

ex : LQ vector RQ	{ $$=$2; }
vector :			{ $$=new Vector(); }
	| vector ex		{ $$=$1; $$->push($2); }
%%