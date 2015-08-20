Lab 02

def cycle(f1, f2, f3):
    def another(x):
        def ret(x):
          i = 0
          while i < n:
          if x == 0:
            return 
        elif n == 1:
            return f1(x)
        elif n == 2:
            return f2(f1(x))
        elif n == 3:
            return f3(f2(f3(x)))
        elif n == 4:
            return f1(f3(f2(f3(x))))
     return another(n)

     I Heard You Liked Functions So I Put Functions In Your Functions
Define a function cycle which takes in three functions as arguments: f1, f2, f3. cycle will then return another function. The returned function should take in an integer argument n and do the following:

Return a function that takes in an argument x and does the following:
if n is 0, just return x
if n is 1, apply the first function that is passed to cycle to x
if n is 2, the first function passed to cycle is applied to x, and then the second function passed to cycle is applied to the result of that (i.e. f2(f1(x)))
if n is 3, apply the first, then the second, then the third function (i.e. 3(f2(f1(x))))
if n is 4, apply the first, then the second, then the third, then the first function (i.e. f1(f3(f2(f1(x)))))
And so forth.
Hint: most of the work goes inside the most nested function.

def cycle(f1, f2, f3):
    """ Returns a function that is itself a higher order function
    >>> def add1(x):
    ...     return x + 1
    ...
    >>> def times2(x):
    ...     return x * 2
    ...
    >>> def add3(x):
    ...     return x + 3
    ...
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    "*** YOUR CODE HERE ***"
Toggle Solution
def cycle(f1, f2, f3):
  def ret_fn(n):
    def ret(x):
      i = 0
      while i &lt; n:
        if i % 3 == 0:
          x = f1(x)
        elif i % 3 == 1:
          x = f2(x)
        else:
          x = f3(x)
        i += 1
      return x
    return ret
  return ret_fn




"""Need to review newtons method"