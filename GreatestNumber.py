x = int(input('Enter 1st Number:'))
y = int(input('Enter 2st Number:'))
z = int(input('Enter 3st Number:'))

if x>y:
    print(x)
elif y>z:
    print(y)
elif z>x:
    print(z)
    print('Bye')
else:
    print('Something went wrong please check your input')
    print('bye')
