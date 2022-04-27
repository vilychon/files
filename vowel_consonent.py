# file=open("vowel_consonent.txt","r")
# a=file.read()
# print(a)
# consonent=0
# vowel=0
# i=0
# while i<len(a):
#     if a[i]in("a","e","i","o","u"):
#         vowel=vowel+1
#     else:
#         consonent=consonent+1
#     i=i+1
# print(vowel)
# print(consonent)

user=input("enter file name:")
f=open(user,"r")
u=f.read().split()
print(u)
i=0
max=u[i]
while i<len(u):
    if len(u[i])>len(max):
        max=u[i]
    i=i+1
print(max)
f.close()
