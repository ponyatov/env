#ifndef _H_ENV
#define _H_ENV

struct Env:Sym { Env(string); };	// \ environment
extern Env *env;					// <env:global>
extern void env_init();				// / init

#endif // _H_ENV
