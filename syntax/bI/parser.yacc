%{
#include "core/hpp.hpp"
%}
%defines %union { Sym*o; }
%token <o> SYM NUM STR				/* scalars: symbol number string	*/
%token <o> LP RP LQ RQ LC RC		/* brackets: () [] {}				*/
%token <o> EQ AT COLON MOD			/* operators: =	@ :	%				*/
%token <o> ADD SUB MUL DIV POW		/* + - * / ^						*/
%token <o> LESS GREAT				/* < >								*/
%token <o> EMAIL URL SKYPE DOMAIN	/* network literals					*/
%token <o> EOL						/* marks end of expression			*/
%type <o> ex scalar	vector 			/* expression scalar vector			*/
%type <o> email skype
%%
REPL : | REPL ex	{ cout << $2->dump();
					  cout << "\n---------------------";
					  cout << $2->eval(env)->dump();
					  cout << "\n---------------------";
					  cout << env->dump();
					  cout << "\n====================================\n"; }

ex : scalar
scalar : SYM | NUM | STR

ex : SYM COLON SYM		{ $$=new Sym($1->val,$3->val); }
ex : ex MOD SYM EQ ex	{ $$=$1; $$->attr[$3->val]=$5; }

ex : LP ex RP			{ $$=$2; }
ex : ex EQ ex			{ $$=$2; $$->push($1); $$->push($3); }

ex : ex DIV ex			{ $$=$2; $$->push($1); $$->push($3); } ;

ex : LQ vector RQ		{ $$=$2; }
vector :				{ $$=new Vector(); }
	| vector ex			{ $$=$1; $$->push($2); }
	| vector SYM EQ ex	{ $$=$1; $$->attr[$2->val]=$4; }
	
ex : LESS email GREAT	{ $$=$2; } | email
email : SYM AT DOMAIN	{ $$=new Email($1,$3); }

ex : skype
skype : SKYPE DOMAIN	{ $$=new Skype($2->val); }
%%