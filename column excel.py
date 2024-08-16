#Leet code question no. 168
a=int(input("Enter the column number: "))
temp=a
b="A B C D E F G H I J K L M N O P Q R S T U V W X Y Z"
c=b.split(" ")
arr=[]
while temp!=0:
    d=temp%26
    d=26 if d==0 else d
    arr.insert(0,d)
    temp=int((temp-1)/26)
print(arr)
result=""
for x in arr:
    result+=c[x-1]
print(result)


