#Leet code question 624
ip=[[1,2,3],[4,5],[2,3,4]]
ip=eval(input("Enter in format [[1,2],[3],[2,5,6]]: "))
mn=max(ip[0])
mx=min(ip[0])
for x in ip:
    mn=min(x) if mn>min(x) else mn
    mx=max(x) if mx<max(x) else mx
print(mn,mx)
print("Maximum distance is",mx-mn)
