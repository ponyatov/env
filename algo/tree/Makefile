go: tree.log

%.log: %.py Makefile
	python $< > $@ && tail $(TAIL) $@
