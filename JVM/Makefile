log.log: src.src Mumbler.class Makefile
	java Mumbler src.src > log.log && tail $(TAIL) $@

%.class: %.java
	javac $<