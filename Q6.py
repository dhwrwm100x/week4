a=str(input("enter string : "))
b=str(input("enter string : "))
if b in a:
    a=a.replace(b,"",1)
    print('text after',a)
else:
    print('substring not found')
