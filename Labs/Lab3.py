
 ### I need to review these alot
 ### I need a lot of recursion practice
 ### excercise 7 and 8;

def sum(n):
  if n == 0:
    return 0
  return n + sum(n-1)

def ab_plus_c(a, b, c):
  if b == 0:
    return c
  return a + ab_plus_c(a, b - 1, c )

def summation(n, term):
  if n == 0:
    return term(0)
  return term(n) + summation(n-1, term)

def hailstone(n):
  print (n)
  if n == 1:
    return 1
  elif n % 2 == 0:
    return 1 + hailstone(n/2)
  else:
    return 1 +hailstone(n*3 + 1)

def repeated(f, n):
  if n == 0:
    return lambda x: x
  return compose1(f, repeated(f, n-1))

 

def falling(n, k):
  
  sum = 1
  while k > 0:
    sum = sum * (n)
    n , k =  n - 1, k - 1
  return sum

def falling1(n, k):
  total, stop = 1, n-k
  while n > stop:
    total, n = total*n, n-1
  return total