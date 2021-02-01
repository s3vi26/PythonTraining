import random

# Problem 1

def gensquares(num):

    for x in range(num):
      yield x**2

for x in gensquares(10):
  print(x)

# Problem 2

def rand_num(low, high, n):

  for n in range(n):
    yield random.randint(low, high)

for num in rand_num(1,10,12):
  print(num) 

# Problem 3

s = 'Hello'

s_iter = iter(s)

print(next(s_iter))
print(next(s_iter))