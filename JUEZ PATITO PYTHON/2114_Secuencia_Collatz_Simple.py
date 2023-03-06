n=int(input())
for i in range(n):
	numero=int(input())
	sumador=0
	while(numero!=1):
		if(numero%2==0):
			numero=numero//2
		else:
			numero=numero+1	
		sumador=sumador+1
	print(sumador)