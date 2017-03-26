def fibonacci(limit):
    nums = []

    current = 0
    next = 1

    while current < limit:
        current, next = next, next + current
        nums.append(current)

    return nums

for n in fibonacci(100):
    print(n, end=', ')

print()


def fibonacci_co():

    current = 0
    next = 1

    while True:
        current, next = next, next + current
        yield current

    # return nums

print('with yield')
for n in fibonacci_co():
    if n > 1000:
        break

    print(n, end=', ')
