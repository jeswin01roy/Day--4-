a= input("enter a string:")
l=len(a)
b=a[ : :-1]
count=0
for i in range(0,l,1):
    if(a[i]!=b[i]):
        count=count+1
    else:
        count=0
if(count==0):
    print(a," is a pallendrome string")
else:
    print(a," is a not a pallendrome string")