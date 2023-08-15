n=int(input('Enter a number:'))
f=1
for i in range(n,0,-1):
    f*=i
print(n,'!','=',n,'*',n-1,'*',n-2,'*',n-3,'*',n-4,'=',f)
