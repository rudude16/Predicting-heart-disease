def isArmstrong(num):
    temp=num
    sum=0
    while(temp!=0):
        r=temp%10
        sum+=r**3
        temp//=10
    if(sum==num):
        return True
    else:
        return False
num=int(input())
if(isArmstrong(num)):
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")
        

