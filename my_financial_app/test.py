import random

def f(one_number):
    return one_number

j = 0

def my_func(n):
    for i in range(0,n):
        x = random.uniform(0, 1)
        y = random.uniform(0, 1)
        if y<f(x):
            j += 1
    return j