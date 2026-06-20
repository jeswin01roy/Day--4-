print("\t\tarmstrong number check")
num = input("enter a number:")
temp = int(num)
dig=len(num)
arno=0
#print(dig)
while(temp>0):
    rem=temp%10
    arno= arno + (rem**dig)
    temp= temp//10
if(int(num)==arno):
    print(num,"is armstrong number")
else:
    print(num,"is not a armstron number")
    
