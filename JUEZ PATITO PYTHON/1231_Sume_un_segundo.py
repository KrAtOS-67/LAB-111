h,m,s=map(int,input().split()) 
cs=s+(m*60)+(h*3600)+1
h=cs//3600
t=cs%3600
m=t//60
s=t%60
print("{:02d}:{:02d}:{:02d}".format(h%24, m, s))