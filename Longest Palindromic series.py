i=input("Enter the string: ")
p=0
for y in range(len(i),1,-1):
    for x in range(len(i)-y+1):
        left=i[x:x+y]
        right=left[::-1]
        if left==right:
            p=1
            break
    if p==1:
        break
print(left)
