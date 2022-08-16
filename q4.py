# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181

def fib(x):
    fibList = [0, 1]
    y = x
    iter = 0
    while x > 0:
        fibList.append(fibList[-1] + fibList[-2])
        x -= 1
        iter += 1
        print(f"Iteration {iter}: {fibList[iter - 1]}")
    print(fibList[:y])
fib(10)