%{
#include "core/hpp.hpp"
%}
%defines %union { Sym*o; }
%token <o> SYM						/* scalars: symbol			*/
%token <o> EQ AT					/* operators: =	@			*/
%token <o> LESS GREAT				/* < >						*/
%token <o> LP RP LQ RQ LC RC		/* brackets: () [] {}		*/
%token <o> EMAIL URL SKYPE DOMAIN	/* network literals			*/
%type <o> ex scalar	vector 			/* expression scalar vector	*/
%type <o> email skype
%%
REPL : | REPL ex	{ cout << $2->dump() << endl; }

ex : scalar
scalar : SYM

ex : LP ex RP		{ $$=$2; }
ex : ex EQ ex		{ $$=$2; $$->push($1); $$->push($3); }

ex : LQ vector RQ	{ $$=$2; }
vector :			{ $$=new Vector(); }
	| vector ex		{ $$=$1; $$->push($2); }
	
ex : LESS email GREAT { $$=$2; } | email
email : SYM AT DOMAIN	{ $$=new Email($1,$3); }

ex : skype
skype : SKYPE DOMAIN	{ $$=new Skype($2->val); }
%%