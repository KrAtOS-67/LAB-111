a,b,c=map(int,input().split())
total=a+b+c
menor=min(a,b,c)
mayor=max(a,b,c)
print(menor,total-menor-mayor,mayor)
