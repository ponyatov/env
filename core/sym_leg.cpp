#include "core/leg.hpp"

Sym::Sym(string V) { val=V; }

string Sym::head() { return "<"+val+">"; }
string Sym::pad(int n) { string S; for (int i=0;i<n;i++) S += '\t'; return S; }
string Sym::dump(int depth) { string S = "\n"+pad(depth)+head();
	return S; }
