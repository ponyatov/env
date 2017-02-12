cpp.log : src.src ./exe.exe Makefile
	./exe.exe < $< > $@ && tail $(TAIL) $@
C = cpp.cpp ypp.tab.cpp lex.yy.c
C += core/sym.cpp core/error.cpp core/int.cpp
C += core/num.cpp core/op.cpp core/env.cpp 
H = hpp.hpp ypp.tab.hpp meta.hpp
CXXFLAGS += -std=gnu++11 -I.
./exe.exe : $(C) $(H)
	$(CXX) $(CXXFLAGS) -o $@ $(C)
ypp.tab.cpp : ypp.ypp
	bison $<
lex.yy.c : lpp.lpp
	flex $<

PY = core/__init__.py core/parser.py core/sym.py core/int.py core/num.py
PY += core/op.py  
py.log : src.src $(PY) Makefile
	python -c "import core" < $< > $@ && tail $(TAIL) $@
