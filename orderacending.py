print("\t\tConverting the list to acending order or decending order")
n= int(input("enter the number of element:"))
list=[]
for i in range(0,n,1):
    a= int(input(f"enter the element {i+1}:"))
    list.append(a)

print(list)
temp=0
for k in range(0,n-1,1):
    if(list[k]>list[k+1]):
        temp=list[k]
        list[k]=list[k+1]
        list[k+1]=temp

print(list)