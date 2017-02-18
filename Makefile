#author/dponyatov.log : author/dponyatov ./exe.exe
#	./exe.exe < $< > $@
#
#cpp.log : src.src ./exe.exe Makefile py.log
#	./exe.exe < $< > $@ && tail $(TAIL) $@
#C = cpp.cpp ypp.tab.cpp lex.yy.c
#C += core/sym.cpp core/error.cpp core/int.cpp
#C += core/num.cpp core/op.cpp core/env.cpp 
#H = hpp.hpp ypp.tab.hpp meta.hpp
#CXXFLAGS += -std=gnu++11 -I.
#./exe.exe : $(C) $(H)
#	$(CXX) $(CXXFLAGS) -o $@ $(C)
#ypp.tab.cpp : ypp.ypp
#	bison $<
#lex.yy.c : lpp.lpp
#	flex $<
#
#PY = core/__init__.py core/parser.py core/sym.py core/int.py core/num.py
#PY += core/op.py  
#py.log : src.src $(PY) Makefile
#	python -c "import core" < $< > $@ && tail $(TAIL) $@

bin/leg.exe: \
		src/peg-0.1.18/src/leg.c \
		src/peg-0.1.18/src/tree.c \
		src/peg-0.1.18/src/compile.c
	gcc -o $@ $?
src/peg-0.1.18/src/leg.c: gz/peg-0.1.18.tar.gz
	cd src && tar zx < ../$<
	touch $@
gz/peg-0.1.18.tar.gz:
	wget -c -P gz http://piumarta.com/software/peg/peg-0.1.18.tar.gz
