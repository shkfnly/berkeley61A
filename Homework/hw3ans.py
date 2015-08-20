def g(n):
  if n < 0:
    return 0
  elif n <= 3:
    return n
  return g(n - 1) + 2 * g(n - 2) + 3 * g(n - 3)

def g_iter(n):
  total = 0
  k = 0
  while k < n:
    if n <= 3:
      return n
    else:
      total = n +  

def has_seven(k):
  if k < 7:
    return False
  elif (k % 10) == 7:
    return True
  return has_seven(k//10) 

def helper(k):
  if k < 7:
    return False
  elif k % 7 ==0:
    return True
  elif (k % 10) == 7:
    return True
  return has_seven(k//10) 

def pingpong(n):
  if n <= 7:
    return n
  return pingpong(n - 1)

def ten_pairs(n):
  if n < 10:
    return 0 
  elif
    return ten_pairs(n//10) + count_digit(n//10, 10 - n%10)

def count_change(n):
  if n == 1:
    return 1
  else:
    return count_change(n - )




f(2)(5)(mul)

3 c and d




