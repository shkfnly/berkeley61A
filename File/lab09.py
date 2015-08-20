class IteratorRestart(object):
  def __init__(self, start, end):
    self.end = end
    self.current = start
    self.begin = start


  def __next__(self):
    if self.current >= self.end:
      raise StopIteration
    self.current += 1
    return self.current - 1

  def __iter__(self):
    self.current = self.begin
    return self