n=input()
asci=ord(n)
if(asci>=97 and asci<=122):
    print("Es letra minúscula.")
elif(asci>=65 and asci<=90):
    print("Es letra mayúscula.")
elif(asci>=48 and asci<=57):
    print("Es numero.")
else:
    print("No es letra ni número.")