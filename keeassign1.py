kurta=400
dupatta=200
pant=600
print("welcome to trends")
cname=input("enter customer name")
cphnno=input("enter phn no")
kurtaq=int(input("enter no. of kurtas"))
dupattaq=int(input("enter no. of dupattas"))
pantq=int(input("enter no.of pants"))
bill=(kurta*kurtaq)+(dupatta*dupattaq)+(pant*pantq)
if(bill>=1000):
        disc=bill*10/100
elif(bill>=2000):
         disc=bill*8/100
elif(bill>=3000):
          disc=bill*5/100
else:
     disc=0
price=bill-disc
gst=price*12/100
amount=price+gst
print("customer no",cphnno)    
print("customer name", cname)
print("bill to be paid",amount)
print("THANK YOUUU")
