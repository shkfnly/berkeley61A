# Name:
# Email:


def square(x):
    """Return x squared."""
    return x * x

# Q1.

def product(n, term):
    """Return the product of the first n terms in a sequence.

    term -- a function that takes one argument

    >>> product(4, square)
    576
    """
    total, k = 1 , 1
    while k <= n:
    	total, k = total * term(k), k + 1
    return total

def factorial(n):
   return product(n, identity)
   """lamba k: k"""


def accumulate(combiner, start, n, term):
    total, k = start, 1
    while k <= n:
        total, k = combiner(term(k), total), k + 1
    return total

from operator import add
def summation_using_accumulate(n, term):
    return accumulate(add, 0, n, term)

from operator import mul
def product_using_accumulate(n, term):
    return accumulate(mul, 1, n, term)

def double(f):
    def twice(x):
        return f(f(x))
    return twice

def repeated(f, n):
    def repeat(x):
        k = 0
        while k < n:
            x, k = f(x) , k + 1
            k += 1
    return repeat
### confused about the usage of X and N in repeated
### Church numerals challenge to do as well.







