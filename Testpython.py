def fact(n):
    if n == 0: return 1
    return n * fact(n - 1)


t = int(input('Enter test case: '))
while t > 0:
    n = int(input('Enter a number: '))
    print(f"{n}'th factorial number is: {fact(n)}")
    t -= 1