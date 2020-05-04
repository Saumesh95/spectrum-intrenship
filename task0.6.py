def fibonacci_seq(n):
    a = 0
    b = 1
    if n == 1:
        print(a)
    elif n == 2:
        print(a,b)
    else:
        print(a,b,end=' ')

    for i in range(n-2):
        c = a + b
        a = b
        b = c
        print(b,end=' ')

    for i in range(0,num**2):
        j = i**2
        if ((5*num**2) + (4)) == j:
            print(f'\n{num} is a fibonacci number')
            break
    else:
        print(f'\n{num} is not a fibonacii number')
            

num = int(input('enter a number : '))
fibonacci_seq(num)