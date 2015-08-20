def make_fib():
    """Returns a function that returns the next Fibonacci number
    every time it is called.

    >>> fib = make_fib()
    >>> fib()
    0
    >>> fib()
    1
    >>> fib()
    1
    >>> fib()
    2
    >>> fib()
    3
    """
    "*** YOUR CODE HERE ***"
    curr, nex1 =  0, 1
    def fib():
        nonlocal curr, nex1
        result = curr
        curr, nex1 = nex1, nex1 + curr
        return result
    return fib

def make_test_dice(seq):
    """Makes deterministic dice.

    >>> dice = make_test_dice([2, 6, 1])
    >>> dice()
    2
    >>> dice()
    6
    >>> dice()
    1
    >>> dice()
    2
    >>> other = make_test_dice([1])
    >>> other()
    1
    >>> dice()
    6
    """
    "*** YOUR CODE HERE ***"
    position = 0
    def dice():
        nonlocal position
        curr = position % len(seq)
        position += 1
        return seq[curr]
    return dice

