import java.io.Console;

// Mumbler Lisp @
// http://cesquivias.github.io/blog/2014/10/13/writing-a-language-in-truffle-part-1-a-simple-slow-interpreter/

class Mumbler {
	public static void main(String[] args) {
		if (args.length == 0)
			REPL();
		else
			LISP(args[0]);
	}

	private static void REPL() {
		System.out.println("REPL:");
		Env global = Env.getBaseEnv();
		Console console = System.console();
		while (true) {
			// READ
			String cmd = console.readLine("> ");
			if (cmd == null) break; // EOF
				// NodeList<AST> nodes = Reader.parse(new ByteArrayInputStream(cmd.getBytes()));
			// EVAL
				// Object result = ListNode.EMPTY;
				// for (AST node:nodes) result = node.eval(global);
			// PRINT
				// if (result != NodeList.EMPTY) System.outn.println(result);
		} // LOOP
	}

	public static void LISP(String fileName) {
		System.out.println("from file: " + fileName);
		Env global = Env.getBaseEnv();
		// NodeList<AST> nodes = Reader.parse(new FileInputStream(fileName));
		// for (AST node : nodes)
		// node.eval(global);
	}
}
