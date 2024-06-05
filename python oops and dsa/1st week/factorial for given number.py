#factorial:
a=int(input("enter number for factorial :"))
series=[]
for i in range(1,a//2+1):
    if a%i==0:
        series.append(i)
series.append(a)
print(series)
