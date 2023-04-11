k=float(input("Tieu thu="))
VAT=0.1
if 1<=k<=100:
    print("Phai tra="+ str(k*550+VAT*(k*550)))
elif 101<=k<=150:
    print("Phai tra="+ str(100*550+(k-100)*750+VAT*(100*550+(k-100)*750)))
elif 151<=k<=200:
   print("Phai tra="+ str(100*550+50*750+(k-150)*950+VAT*(100*550+50*750+(k-150)*950)))
else: print("Phai tra="+ str(100*550+50*750+50*950+(k-200)*1350+VAT*(100*550+50*750+50*950+(k-200)*1350)))
