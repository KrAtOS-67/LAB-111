n=int(input())
for i in range(n):
	numero=int(input())
	if(numero==1):
		print(1)
	else:
		print(str((numero-1)**3) + "+" + str(numero**3))