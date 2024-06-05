#codeforces 617a question elephant
a=int(input("enter the number"))
b=a%5
if b>0:
    print((a//5)+1)
else:
    print(a//5)