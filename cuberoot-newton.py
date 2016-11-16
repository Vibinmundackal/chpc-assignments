i=input('Enter the number ')
x=0.3*i
error=0.000000001
while(abs((x**3)-i)>error):
fx=(x**3)-i
dfx=3*(x**2)
x=x-(fx/dfx)
print 'Cube root: ',x
