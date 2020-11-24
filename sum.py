
def sum1(n):
    num = 0
    for i in range(n+1):
        num += i
    print(num)


print("Sum1: ")
sum1(10)


def sum2(n):
    sum = 0
    i = 0
    while i <= n:
        sum = sum + i
        # print(sum)
        i += 1
    print(sum)


print("Sum2: ")
sum2(10)


def sum3(n):
    print(sum(range(n+1)))


print("Sum3: ")
sum3(10)


def sum4(n):
    if n == 1:
        return n
    return n + sum4(n+1)


print(sum4(10))
