log.log: src.src ./exe.exe
	./exe.exe < $< > $@ && tail $(TAIL) $@

# by default use JIT compiler mode for TCC backend
# run " (mingw32-)make JIT=EXE " for .exe compiling
JIT ?= -DJIT=RAM
# TCC libraries
TCC = $(JIT) -Ilibtcc -Llibtcc libtcc.dll
# required .dll
libtcc.dll: libtcc/libtcc.dll
	cp $< $@
lib/libtcc1.a: libtcc/libtcc1.a	
	mkdir -p lib ; cp $< $@

C = cpp.cpp ypp.tab.cpp lex.yy.c
H = hpp.hpp ypp.tab.hpp
L += $(TCC)
CXXFLAGS += -std=gnu++11
./exe.exe: $(C) $(H) Makefile libtcc.dll lib/libtcc1.a
	$(CXX) $(CXXFLAGS) -o $@ $(C) $(L)
ypp.tab.cpp: ypp.ypp
	bison $<
lex.yy.c: lpp.lpp
	flex $<

