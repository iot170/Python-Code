x = int(input('Enter a number to check Even or Odd:'))
r = x % 2

if r==0:
    print("Even")
    if x>5:
        print("Great")
    else:
        print("Not so great")
else:
    print("Odd")
print('Bye')