#codeforces 4a question watermelon new
h=int(input("enter the number"))
if (h%2 !=0 or h<4):
    print("no")
else:
    x=h//2
    if(x%2==0):
        print("height of 2 pieces are:",x,x)
    else:
        print("height of 2 pieces are:",x-1,x+1)