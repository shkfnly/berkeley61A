class IteratorRestart(object):
    """
    >>> i = IteratorRestart(2, 7)
    >>> for item in i:
    ...     print(item)
    2
    3
    4
    5
    6
    7
    >>> for item in i:
    ...     print(item)
    2
    3
    4
    5
    6
    7
    """
    def __init__(self, start, end):
        "*** YOUR CODE HERE ***"
        self.end = end
        self.current = start
        self.begin = start

    def __next__(self):
        "*** YOUR CODE HERE ***"
        if self.current >= self.end:
            raise StopIteration
        self.current += 1
        return self.current - 1
    def __iter__(self):
        "*** YOUR CODE HERE ***"
        self.current = self.begin
        return self

def countdown(n):
    """
    >>> for number in countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """

    n = 5
    while n >= 0:
        yield n
        n -= 1

class Countdown(object):
    """
    >>> for number in Countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    def __init__(self, number):
        self.number = number
   
    def __iter__(self):
        while self.cur > 0:
            yield self.cur
            self.cur -= 1



def hailstone(n):
    """
    >>> for num in hailstone(10):
    ...     print(num)
    ...
    10
    5
    16
    8
    4
    2
    1
    """
    i = n
    while i > 1:
        yield i
        if i % 2 == 0:
            i //= 2
        else:
            i = i * 3 + 1
    yield i



