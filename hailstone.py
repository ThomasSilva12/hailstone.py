### Thomas Silva
### ENGR 103 project 4c.

def hailstone(n):
    if n == 1:
        return 0  #

    steps = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
        steps += 1

    return steps

# Test the function
print(hailstone(1000))

