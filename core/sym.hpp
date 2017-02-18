#ifndef _H_SYM
#define _H_SYM

#include "core/leg.hpp"
struct Sym {
	string val;
	Sym(string);
	virtual string dump(int=0);
	virtual string head();
	string pad(int);
};

#endif // _H_SYM
