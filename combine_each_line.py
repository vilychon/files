file1=open("file.txt","r")
file2=open("file2.txt","r")
file3=open("merge.txt","w")
line1=file1.readlines()
line2=file2.readlines()
for i in range (len(line1)):
    merged=line1[i]+line2[i]
    file3.write(merged)
file1.close()
file2.close()
file3.close()

