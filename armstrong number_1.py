n=int(input('Enter a number:'))
t=n

c=0
while t>0:
    c+=1
    t//=10

t=n
s=0
while t>0:
    d=t%10
    s+=d**c
    t//=10

if s==n:
    print('armstrong number')
else:
    print('not armstrong number')
