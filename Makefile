tmp/dponyatov.log: author/dponyatov bin/bI.exe
	bin/bI.exe < $< > $@ && tail $(TAIL) $@
C = core/main.cpp tmp/bI.lexer.cpp tmp/bI.parser.cpp core/error.cpp \
	core/sym.cpp core/env.cpp core/str.cpp core/op.cpp core/vector.cpp \
	core/domain.cpp core/login.cpp core/email.cpp core/skype.cpp
H = tmp/bI.parser.hpp core/lex.hpp core/yacc.hpp core/hpp.hpp core/inc.hpp \
	core/sym.hpp core/env.hpp core/str.hpp core/op.hpp core/vector.hpp \
	core/domain.hpp core/login.hpp core/email.hpp core/skype.hpp
CXXFLAGS += -std=gnu++11 -I. -O0 -g0 -pipe
bin/bI.exe: $(C) $(H)
	cat $(C) > cpp.cpp
	$(CXX) $(CXXFLAGS) -o $@ cpp.cpp
tmp/bI.lexer.cpp: syntax/bI/lexer.lex
	flex -o$@ $<
tmp/bI.parser.cpp: syntax/bI/parser.yacc
	bison -o$@ $<

##C = cpp.cpp ypp.tab.cpp lex.yy.c
##C += core/sym.cpp core/error.cpp core/int.cpp
##C += core/num.cpp core/op.cpp core/env.cpp 
##H = hpp.hpp ypp.tab.hpp meta.hpp
##ypp.tab.cpp : ypp.ypp
##	bison $<
##lex.yy.c : lpp.lpp
##	flex $<
##
##PY = core/__init__.py core/parser.py core/sym.py core/int.py core/num.py
##PY += core/op.py  
##py.log : src.src $(PY) Makefile
##	python -c "import core" < $< > $@ && tail $(TAIL) $@
#
# : author/dponyatov bin/bI.exe
#	bin/bI.exe < $< > $@ && tail $@
#
#C = tmp/bI.cpp core/sym_leg.cpp
#H = core/leg.hpp core/inc.hpp core/sym.hpp
#bin/bI.exe: $(C) $(H)
#	$(CXX) -I. -o $@ $(C)
#tmp/bI.cpp: syntax/bI/leg bin/leg.exe Makefile
#	bin/leg.exe -o $@ $<
#
#bin/leg.exe: \
#		src/peg-0.1.18/src/leg.c \
#		src/peg-0.1.18/src/tree.c \
#		src/peg-0.1.18/src/compile.c
#	gcc -o $@ $^
#src/peg-0.1.18/src/leg.c: gz/peg-0.1.18.tar.gz
#	cd src && tar zx < ../$<
#	touch $@
#gz/peg-0.1.18.tar.gz:
#	wget -c -P gz http://piumarta.com/software/peg/peg-0.1.18.tar.gz
