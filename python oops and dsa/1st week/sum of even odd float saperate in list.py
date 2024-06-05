list1=[1,2,3,4,1.3,3.2]
a=0
b=0
c=0
for i in range(len(list1)):
    if list1[i]%2==0:
        a+=list1[i]
    elif list1[i]%2==1:
        b+=list1[i]
    else:
        c+=list1[i]
print("even sum =",a)
print("odd sum =",b)
print("float sum =",c)
