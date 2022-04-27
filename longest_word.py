# user=(input("enter the name:"))
# file=open(user)
# a=file.read()
# b=a.split()
# print(b)
# max=b[0]
# i=0
# while i<len(b):
#     if len(b[i])>len(max):
#         max=b[i]
#     i=i+1
# print("longest word is:")


user=input("enter the name:")
file=open(user)
a=file.readlines()
b=a.split()
print(b)
max=b[0]
i=0
while i<len(b):
    if len(b[i])<len(max):
        max=b[i]
    i=i+1
print("longest word is:")
