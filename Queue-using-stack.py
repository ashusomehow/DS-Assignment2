class Queue:
  def __init__(self):
    self.input = []
    self.output = []

  def push(self, x: int) -> None:
    self.input.append(x)

  def pop(self) -> int:
    self.peek()
    return self.output.pop()

  def peek(self) -> int:
    if not self.output:
      while self.input:
        self.output.append(self.input.pop())
    return self.output[-1]

  def empty(self) -> bool:
    return not self.input and not self.output
        


# Your Queue object will be instantiated and called as such:
# obj = Queue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()