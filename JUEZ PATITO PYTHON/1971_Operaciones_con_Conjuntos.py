import sys
for entrada in sys.stdin:
	a,b=map(int,entrada.split())
	print(a|b,a&b,(a|b)^b)

