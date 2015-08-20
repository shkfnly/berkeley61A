discussion 2


def find_quartile(x):

    if x > 75:
        print (Q1)

    elif x >= 50:
        print (Q2)

    elif x > 25:
        print (Q3)
    else:
        print (Q4)

  if x > 0:
      if x > 25:
          if x > 50:
              if x > 75:
                  print ("Q4")
                  return
              print("Q3")
              return
          print("Q2")
          return
      print("Q1")

def is_prime(n):
  k = n - 1
  while k > 1:
    if n % k == 0:
      return False
    k -= 1
  return True
 ### this should work however it would run for a much longer time than starting with smaller nubmers

  k = 2
  while k < n:
    if n % k == 0:
      return False
    k += 1
  return True

  def square_every_number(n):
    k = 1
    while k <= n:
      print (square(k))
      k += 1

def double_every_number(n):
    k = 1
    while k <= n:
      print (double(k))
      k += 1
def every(func, n):
  k = 1
  while k <= n:
    print(func(k))
    k += 1

def keep(cond, n):
  k = 1
  while k <= n:
    if cond(i):
      print(k)
    k += 1

def and_add_one(f):
  def add_one(g):
    return f(x) + 1
  return add_one

def and_add(f, n):
  def foo(x):
    return f(x) + n
  return foo

  """go over currying"""





