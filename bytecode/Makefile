log.log: bin.bin ./exe.exe
	./exe.exe   $< >> log.log && tail $(TAIL) $@
bin.bin: src.src ./exe.exe
	./exe.exe < $< >  log.log
C = cpp.cpp ypp.tab.cpp lex.yy.c
H = hpp.hpp ypp.tab.hpp
CXXFLAGS += -std=gnu++11
./exe.exe: $(C) $(H)
	$(CXX) $(CXXFLAGS) -o $@ $(C)
ypp.tab.cpp: ypp.ypp
	bison $<
lex.yy.c: lpp.lpp
	flex $<	
