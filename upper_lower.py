# file=open("upper_lower.txt")
# a=file.read()
# print(a)
# upper=0
# lower=0
# i=0
# while i<len(a):
#     if a[i].isupper():
#         upper+=1
#     else:
#         lower+=1
#     i=i+1
# print(upper)
# print(lower)

file=open("upper_lower.txt","r")
a=file.read()
print(a)
upper=0
lower=0
i=0
while i<len(a):
    if a[i].isupper():
        upper+=1
    else:
        lower+=1
    i=i+1
print(upper)
print(lower)

