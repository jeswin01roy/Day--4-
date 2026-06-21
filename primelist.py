print("\t\tprime and composit")
start,stop= int(input("enter the number starting range:")),int(input("enter the number starting range:"))
listp=[]
listc=[]
for i in range(start,stop+1,1):
    if(start==1):
        print("1 is neither prime nor composit")

    elif(start>=2):
        count=0
        for j in range(2,i,1):
            if(i%j==0):
                count=count+1
    
        if(count==0):
            listp.append(i)
        else:
            listc.append(i)
    else:
        print("invalid entry at start!")
        break
print("prime numbers\n",listp)

print("\n composit numbers\n",listc)

        