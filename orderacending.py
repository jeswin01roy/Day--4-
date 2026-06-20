print("\t\tConverting the list to ascending order or descending order")
n= int(input("enter the number of element:"))
list=[]
for i in range(0,n,1):
    a= int(input(f"enter the element {i+1}:"))
    list.append(a)
print(list)
r= int(input("Select ascending or descending order (ascending-0 & descending-1):"))
temp=0
if(r==0):
    for i in range(n-1):
        for k in range(n-i-1):
            if(list[k]>list[k+1]):
                temp=list[k]
                list[k]=list[k+1]
                list[k+1]=temp
elif(r==1):
    for i in range(n-1):
        for k in range(n-i-1):
            if(list[k]<list[k+1]):
                temp=list[k]
                list[k]=list[k+1]
                list[k+1]=temp
else:
    print("invalid entry")

print(list)
