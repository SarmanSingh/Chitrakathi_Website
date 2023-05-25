import math
for i in range(10000):
    temp=i
    rev=0
    while(temp>0):
        r=temp%10
        rev=rev*10+r
        temp=temp//10
    if(rev==i):
        b=int(math.pow(i,1/3))
        print(b)
        temp2=b
        rev2=0
        while(temp2>0):
            r=temp2%10
            rev2=rev2*10+r
            temp2=temp2//10
        if(b!=rev2):
            print(i)
            print("Its cube root", b," is not a palindrome")


    
    

        
