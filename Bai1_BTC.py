import math
a=float(input("a="))
b=float(input("b="))
c=float(input("c="))
p=(a+b+c)/2
if (a+b)>c and (a+c)>b and (c+b)>a: 
    print("Dien tich="+ str(round(math.sqrt(p*(p-a)*(p-b)*(p-c)), 3)))
else: print("Khong hop le")