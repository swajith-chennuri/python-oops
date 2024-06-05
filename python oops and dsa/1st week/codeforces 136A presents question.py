# https://codeforces.com/problemset/problem/136/A
# 136/A presents
no_of_number=int(input("enter the no of friends"))
listinput=list(map(int,input().split(" ")))
print(listinput)
b=[0]*no_of_number
for i in range(0,no_of_number):
    c=listinput[i]
    b[c-1]=i+1
print(b)