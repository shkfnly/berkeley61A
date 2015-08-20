
## 1
def countdown(n):
  if n == 0:
    return 
  print(n)
  countdown(n - 1)  

##Still need to figure this out##
#2
def countup(n):
  n = -n
  if n == 0:
    return
  countup(n + 1)
  print(n)

#3
def expt(base, power):
  if power == 0:
    return 1
  return base * expt(base, power - 1)

#4
def isprime(n):
  k = 1
  if n == 0:
    return True
  elif k == n:
    return True
  while k < n:
      if n % k != 0:
        k += 1
      else:
        return False

def sum_primes_up_to(n):
  if n == 1:
    return 0
  elif isprime(n) == true:
    return n + sum_primes_up_to(n - 1)
  else:
    return sum_primes_up_to(n - 1)

def sum_filter_up_to(n, pred):
    if n == 0:
      return 0
    elif (pred(n)):
      return n + sum_filter_up_to(n - 1, pred)
    else:
      return sum_filter_up_to(n - 1, pred)

def count_stair_ways(n):
  if n == 1:
    return 1
  elif n == 2:
    return 2
  return count_stair_ways(n - 1) + count_stair_ways(n - 2)

def pascal(row, column):
  if row == 0:
    return 1
  elif column == 0:
    return 1
  return pascal(row - 1, column) + pascal(row - 1, column - 1)
def sum_less_than(total, num):
  if num > total:
    return true
  elif num == 0:
    return false 

  return sum_less_than(total - num, num - 1)

def has_sum(amount, n1, n2):
  if amount % n1 == 0:
    return True
  elif amount % n2 == 0:
    return True
  elif amount < n1 and amount < n2:
    return False
  return has_sum(amount - n1, n1, n2) or has_sum(amount - n2, n1, n2)

###one last problem to do
