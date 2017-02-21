import sys ; sys.stdout = open(sys.argv[0]+'.log','w')

# from sym import *
from parse import *

parser.parse('''n-1
# def fib(n) {
# 	if n<=0 ^0
# 	if n<2 ^1
# 	else ^ fib(n-1)+fib(n-2)
# }
# 
# def none(){}
# 
# def main() {
# #none()
# #print fib(11)
# }
''')

