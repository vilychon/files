list=[10,20,10,20,10,10,30,50,10,20]
i=0
while i<len(list):
    j=0
    b=[]
    count=0
    while j<len(list):
        if list[i]==list[j]:
            count+=1
            b.append(list[i])
        j+=1
    print(b)
    i=i+1

    
    