# Various solutions for a Fibonacci sequence generator

# Example of generator function
def generate_cubes(n):
    for n in range(n):
        yield n**2
for n in generate_cubes(10):
    print(n)


def gen_fibonacci_A(n):
    # 0 1 1 2 3 5 8 13 21 34 55 89 ...
    a = 0
    b = 1
    for i in range(n):
        t = a
        a = a + b
        b = t
        yield b
    return
for i,n in enumerate(gen_fibonacci_A(10)):
    print(i,n)


def gen_fibonacci_B(n):
    # 0 1 1 2 3 5 8 13 21 34 55 89 ...
    a = 0
    b = 1
    yield a
    yield b
    for i in range(n):
        t = b
        b = a + b
        a = t
        yield b
    return
for i,n in enumerate(gen_fibonacci_B(_10)):
    print(i, n)


def gen_fibonacci_C(n):
    # 0 1 1 2 3 5 8 13 21 34 55 89 ...
    a = 0
    b = 1
    for i in range(n):
        t = a
        a = a + b
        b = t
        yield b
    yield a
    return
for i,n in enumerate(gen_fibonacci_C(10)):
    print(i,n)


def gen_fibonacci_D(n):
    a = 0
    b = 1
    for i in range(n):
        a,b = b, a+b
        yield b
    yield a
    return
for i,n in enumerate(gen_fibonacci_D(10)):
    print(i,n)
