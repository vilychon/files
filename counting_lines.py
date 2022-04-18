# file=open("count_people.txt","r")
# a=file.readline()
# print(len(a))
# file.close()
file=open("count.txt","r")
m=file.readlines()
i=0
count=0
while i<len(m):
    count+=1
    i=i+1
print(count)
file.close()
