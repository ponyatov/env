#ifndef _H_SYM
#define _H_SYM

struct Sym {
	string tag;					// type/class tag
	string val;					// value: any data can be represented in text
	Sym(string T,string V);		// <T:V> \ constructors
	Sym(string V);				// token /
	vector<Sym*> nest;			// \ nest[]ed elements
	Sym* push(Sym*);			// /
	map<string,Sym*> attr;		// \ attributes
	Sym* lookup(string);		// /
	virtual string dump(int=0);	// \ dump in tree form
	virtual string head();		// <T:V> header
	string pad(int);			// / left pad tree element
//	virtual Sym* eval(Sym*E);	// evaluate/compute object
//	virtual Sym* pfxadd();		// + A
//	virtual Sym* pfxsub();		// - A
//	virtual Sym* add(Sym*);		// A + B
//	virtual Sym* sub(Sym*);		// A - B
//	virtual Sym* mul(Sym*);		// A * B
//	virtual Sym* div(Sym*);		// A / B
//	virtual Sym* pow(Sym*);		// A ^ B
//	virtual Sym* ass(Sym*);		// assert A==B
//	Sym* ok(Sym*);				// test:ok
//	Sym* fail(Sym*);			// test:fail
};

#endif // _H_SYM
