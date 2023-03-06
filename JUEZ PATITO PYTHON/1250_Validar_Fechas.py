def bis(año):
    if año % 4 == 0 and (año % 100 != 0 or año % 400 == 0):
        return True
    else:
        return False
def hora(a,b,c):
    if(b==1 or b==3 or b==5 or b==7 or b==8 or b==10 or b==12):
        if(a<=31 and 1<=a):
            print("Fecha correcta")
        else:
            print("Fecha incorrecta")
    elif(b==4 or b==6 or b==9 or b==11):
        if(a<=30 and 1<=a):
            print("Fecha correcta")
        else:
            print("Fecha incorrecta")
    elif(b==2):
        if(bis(c)):
            if(a<=29 and 1<=a):
                print("Fecha correcta")
            else:
                print("Fecha incorrecta")
        else:
            if(a<=28 and 1<=a):
                print("Fecha correcta")
            else:
                print("Fecha incorrecta")
    else:
        print("Fecha incorrecta")
         
for i in range(int(input())):
    a,b,c=map(int,input().split())
    hora(a,b,c)