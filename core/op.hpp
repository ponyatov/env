#ifndef _H_OP
#define _H_OP

struct Op:Sym { Op(string);	Sym*eval(Sym*) override; };	// operator

#endif // _H_OP
