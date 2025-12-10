for i in range(1,50):
    count=0
    for j in range(i):
        if i%j==0:
            count+=1
    if(count==1):
        print(i)
