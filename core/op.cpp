#include "core/hpp.hpp"

Op::Op(string V):Sym("op",V){}
Sym* Op::eval(Sym*E) {
	if (val!="~") Sym::eval(E); else return nest[0];
	switch (nest.size()) {
//		case 1:
//			if (val=="+") return nest[0]->pfxadd();
//			if (val=="-") return nest[0]->pfxsub();
		case 2:
//			if (val=="+") return nest[0]->add(nest[1]);
//			if (val=="-") return nest[0]->sub(nest[1]);
//			if (val=="*") return nest[0]->mul(nest[1]);
			if (val=="/") return nest[0]->div(nest[1]);
//			if (val=="^") return nest[0]->pow(nest[1]);
//			if (val=="?=") return nest[0]->ass(nest[1]);
	}
	return this; }
