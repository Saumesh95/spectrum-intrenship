a = int(input('enter the lower interval : '))
b = int(input('enter the upper interval : '))
for i in range(a,b+1):
    if i>1:
        for num in range(2,i):
            if (i%num) == 0:
                break
        else:
            print(i,end=' ')

if a>1:
    for i in range(2,a):
        if (a%i) == 0:
            print(f"\n{a} is not a prime number")
            break
    else:
        print(f"\n{a} is a prime number")
else:
    print(f"\n {a} is not a prime number")
        
if b>1:
    for j in range(2,b):
        if (b%j) == 0:
            print(f"{b} is not a prime number")
            break
    else:
        print(f"{b} is a prime number")
else:
    print(f"\n{b} is not a prime number")
        
