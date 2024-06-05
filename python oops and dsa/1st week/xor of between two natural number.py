def xor(n):
    if n%4==0:
        return(n)
    elif (n-1)%4==0:
        return(1)
    elif (n+2)%4==0:
        return(n+1)
    else:
        return(0)
a=int(input("enter 1st number"))
b=int(input("enter 2st number"))
a=xor(a)
print(a)
b=xor(b)
print(b)
print(a^b)