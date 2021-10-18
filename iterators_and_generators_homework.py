#Problem 1

def gensquares(n):
    for x in range(n):
        yield x**2

for x in gensquares(10):
    print(x)


print(*gensquares(10))

#Problem 2

import random

def rand_num(low,high,n):
    how_many_numbers=0
    while how_many_numbers < n:
        yield random.randint(low,high)
        how_many_numbers+=1   

print(*rand_num(1,10,5),sep="\n")

#Problem 3
s="hello"
s_iter=iter(s)
print(next(s_iter))
#Problem 4


#Extra Credit