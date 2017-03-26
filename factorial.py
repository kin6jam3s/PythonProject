def fatorial(n):
    if n == 1:
        return 1

    return n * fatorial(n - 1)

print("5!={:,}, 3!={:,}, 11!={:,}.".format(
    fatorial(5),
    fatorial(3),
    fatorial(11)
))

