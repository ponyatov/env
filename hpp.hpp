
struct Env:Sym { Env(string); };			// \ environment
extern Env *glob;							// <env:global>
extern void glob_init();					// / init

struct Error:Sym { Error(string); Error(Sym*); };	// error

struct Int:Sym {
	Int(string); Int(long); long val;		// integer
	string head(); Sym*eval(Sym*);
	Sym* pfxadd(); Sym* pfxsub();
	Sym* add(Sym*); Sym* sub(Sym*);
	Sym* mul(Sym*); Sym* div(Sym*);
	Sym* pow(Sym*); Sym* ass(Sym*);
	};
struct Num:Sym {							// floating number
	Num(string); Num(double); double val;
	string head(); Sym*eval(Sym*);
	Sym* pfxadd(); Sym* pfxsub();
	Sym* add(Sym*); Sym* sub(Sym*);
	Sym* mul(Sym*); Sym* div(Sym*);
	Sym* pow(Sym*); Sym* ass(Sym*);
	};
