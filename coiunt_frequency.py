def word_frequency():
   file=open("count_frequency.txt","r")
   a=file.read()
   b=a.split()
   i=0
   count=0
   while i<len(b):
      if count in b[i]:
        count+=1
      i=i+1
print("count")

