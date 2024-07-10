class Stack:

    def __init__(self) -> None:
        self.data = []

    def push(self, val):
        self.data.append(val)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def display(self):
        print(self.data)


stack = Stack()

stack.push(1)
stack.push(2)
stack.push(4)
stack.display()
print(stack.top())
# stack
stack.pop()
print(stack.top())
stack.display()