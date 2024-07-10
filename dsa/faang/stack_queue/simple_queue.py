class Queue:

    def __init__(self):
        self.head = 0
        self.data = []

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        if not self.is_empty():
            self.head += 1

    def is_empty(self) -> bool:
        return self.head >= len(self.data)

    def display(self) -> None:
        if not self.is_empty():
            for idx in range(self.head, len(self.data)):
                print(self.data[idx], end='->')
            print()
        else:
            print('Queue is empty!')


q = Queue()
q.display()
q.enqueue(1)
q.enqueue(3)
q.enqueue(5)
q.enqueue(6)
q.display()
q.dequeue()
q.dequeue()
q.display()
print(q.data)