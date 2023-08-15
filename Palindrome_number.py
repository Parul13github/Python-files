n=int(input('Enter a number:'))
r=0
while n>0:
    d=n%10
    r=r*10+d
    n=n//10

print(n,r)

if n==r:
    print('Palindrome number')
else:
     print('Not palindrome number')
#this will revere the number but after the process n will become zero.
#n=0 after the process
