M1=int(input("M1="))
M2=int(input("M2="))
M3=int(input("M3="))
S=int(input("S="))
if S<=100:
    print("Phai tra="+ str(S*M1))
elif 101<=S<=150:
    print("Phai tra="+ str((S-100)*M2+100*M1))
else: print("Phai tra="+ str(100*M1+50*M2+M3*(S-150)))