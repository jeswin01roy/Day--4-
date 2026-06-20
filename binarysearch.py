print("\t\tBinary search")
n= int(input("enter the number of element:"))
list=[]
for i in range(0,n,1):
    a= int(input(f"enter the element {i+1}:"))
    list.append(a)
print(list)
s= int(input("enter the searching element:"))
temp=0
for i in range(n-1):
    for k in range(n-i-1):
        if(list[k]>list[k+1]):
            temp=list[k]
            list[k]=list[k+1]
            list[k+1]=temp
i=0
while i <= n:
    mid = (i + n) // 2

    if list[mid] == s:
        print("the value is found on the index",mid+1)
  

    if list[mid] < s:
        i = mid + 1
    else:
        n = mid - 1
