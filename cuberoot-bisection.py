i=input('Enter the number ')
x=0.0000000001
p=0.0
q= max(1.0,x)
r= (p+q)/ 2.0
while abs(r**3 -i)>= x:
if 'r**3 <= i':
p=q
else:
q= r
r = (q+p)/2.0
print 'The cube root is', r
