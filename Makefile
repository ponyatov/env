log.log : src.src ./exe.exe Makefile
	./exe.exe < $< > $@ && tail $(TAIL) $@