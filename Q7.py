x=[]
while True:
    a=input('enter ')
    if a=="":
        break
    x.append(a)
b="\n".join(x)
c=len(b)-1
w=len(b.split())
l=len(x)
print('characters ',c)
print('words',w)
print('lines',l)
