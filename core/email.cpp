#include "core/hpp.hpp"
Email::Email(Sym*A,Sym*B):Sym("email",""){
	if (A->tag == "login") attr["login"] = A;
	else attr["login"] = new Login(A->val);
	if (B->tag == "domain") attr["domain"] = B;
	else attr["domain"] = new Domain(B->val);
	val = attr["login"]->val +"@"+ attr["domain"]->val;
}
