def prime(n):
    count=0
    for j in range(1,n+1):
        if n%j==0:
            count+=1
    if(count==2):
        return True
    else:
        return False


for i in range(1,50):
    if prime(i)==True:
        print(i)
