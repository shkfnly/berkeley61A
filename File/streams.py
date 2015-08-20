class Stream(object):
    class empty(object):
        def __repr__(self):
            return 'Stream.empty'

    empty = empty()

    def __init__(self, first, compute_rest, empty= False):
        self.first = first
        self._compute_rest = compute_rest
        self.empty = empty
        self._rest = None
        self._computed = False

    @property
    def rest(self):
        assert not self.empty, 'Empty streams have no rest.'
        if not self._computed:
            self._rest = self._compute_rest()
            self._computed = True
        return self._rest

    def __repr__(self):
        return 'Stream({0}, <...>)'.format(repr(self.first))

def make_integer_stream(first=1):
    def compute_rest():
        return make_integer_stream(first+1)
    return Stream(first, compute_rest)

def add_streams(s1, s2):
    "*** YOUR CODE HERE ***"
    def compute_rest():
         return add_streams(s1.rest, s2.rest)
    return Stream(s1.first + s2.first, compute_rest)
   

def make_fib_stream():
    "*** YOUR CODE HERE ***"
    def fib_helper(current, next):
    return Stream(current, Stream(next + current, fib_helper))   
    return fib_stream_generator(0, 1)
def fib_stream_generator(a, b):
    def compute_rest:
        return fib_stream_generator(b, a+b)
    return Stream(a, compute_rest) 



def stream_map(func, stream):
    def stream_map_rest():
        return stream_map(func, stream.rest)
    if Stream.empty:
        return stream
    else:
        return Stream(func(stream.first), stream_map_rest)

def my_stream():
    def compute_rest():
        return add_streams(map_stream(double,
                                      my_stream()),
                                      my_stream())
    return Stream(1, compute_rest)

1 2 4 8 16

def interleave(stream1, stream2):
    "*** YOUR CODE HERE ***"
    if stream1.empty:
        return Stream.the_empty_stream
    return Stream(stream1.first, lambda: interleave(stream2, stream1.rest))