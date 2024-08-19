#Leet code question 172
def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)
n=int(input("Enter the number: "))
print(f"{n}!={fact(n)}")
count=0
for x in str(fact(n))[::-1]:
    if x=="0":
        count+=1
    else:
        break
print("No. of trailing zeros are",count)
    
