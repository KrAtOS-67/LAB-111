import sys
for entrada in sys.stdin:
    a=int(entrada)
    peniques=a%12
    chelines=(a//12)
    libras=chelines//20
    print((libras,chelines%20,peniques))