import sys ; sys.stdout = open(sys.argv[0]+'.log','w')

# from sym import *
from parse import *

parser.parse('''
# def fib(n) {
# 	if n<=0 ^0
# 	if n<2 ^1
# 	else ^ fib(n-1)+fib(n-2)
# }
 
def none(x){ 1+2 ^none(x)}
 
# def main() {
# #none()
# #print fib(11)
# }
''')

