#fibonacci series:
a=int(input("enter number for fibonacci :"))
b,c=0,1
series=[]
for i in range(a):
    series.append(b)
    b,c=c,c+b
print(series)