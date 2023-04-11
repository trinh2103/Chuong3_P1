a=input("a=")
b=input("b=")
c=input("c=")
if a>b and b>c:
    print("SLN="+str(a))
    print("SBN="+str(c))
elif a>c>b:
   print("SLN="+str(a))
   print("SBN="+str(b))
elif b>c>a:
    print("SLN="+str(b))
    print("SBN="+str(a))
elif b>a>c:
    print("SLN="+str(b))
    print("SBN="+str(c))
elif c>a>b:
    print("SLN="+str(c))
    print("SBN="+str(b))
elif c>b>a:
    print("SLN="+str(c))
    print("SBN="+str(a))