go: cpp.log py.log

cpp.log : src.src ./exe.exe Makefile
	./exe.exe < $< > $@ && tail $(TAIL) $@
C = cpp.cpp ypp.tab.cpp lex.yy.c
H = hpp.hpp ypp.tab.hpp meta.hpp
CXXFLAGS += -std=gnu++11
./exe.exe : $(C) $(H)
	$(CXX) $(CXXFLAGS) -o $@ $(C)
ypp.tab.cpp : ypp.ypp
	bison $<
lex.yy.c : lpp.lpp
	flex $<

py.log : src.src py.py Makefile
	python py.py < $< > $@ && tail $(TAIL) $@