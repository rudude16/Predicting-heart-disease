import math
def isPrime(num):
    count=0
    for i in range(1,(int)(math.sqrt(num)+1)) :
        if ((num%i)==0):
            count+=1
    if count==1:
        return True
    else:
        return False
for num in range(100,301):
    if(isPrime(num)):
        print(num)
        

