log.log: src.src ./exe.exe libtcc.dll
	./exe.exe < $< > $@ && tail $(TAIL) $@

# by default use JIT compiler mode for TCC backend
# run " (mingw32-)make JIT= " for .exe compiling
JIT ?= -DJIT
# TCC libraries
TCC = $(JIT) -Ilibtcc libtcc.dll
# required .dll
libtcc.dll: libtcc/libtcc.dll
	cp $< $@

C = cpp.cpp ypp.tab.cpp lex.yy.c
H = hpp.hpp ypp.tab.hpp
L += $(TCC)
./exe.exe: $(C) $(H) Makefile libtcc.dll
	$(CXX) $(CXXFLAGS) -o $@ $(C) $(L)
ypp.tab.cpp: ypp.ypp
	bison $<
lex.yy.c: lpp.lpp
	flex $<


