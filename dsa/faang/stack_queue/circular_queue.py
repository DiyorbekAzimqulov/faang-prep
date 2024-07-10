class CircularQueue:

    def __init__(self, i: int) -> None:
        self.head = -1
        self.tail = -1
        self.size = i
        self.data = [-1 for j in range(i)]

    def enqueue(self, val: int):
        if self.is_full():
            return
        if self.is_empty():
            self.head = 0
        self.tail = (self.tail + 1) % self.size
        self.data[self.tail] = val

    def dequeue(self):
        if self.is_empty():
            return
        if self.head == self.tail:
            self.head = -1
            self.tail = -1
            return
        self.head = (self.head + 1) % self.size

    def is_full(self) -> bool:
        """
        |     |
        1, 2, 3
        """
        return (self.tail + 1) % self.size == self.head

    def is_empty(self) -> bool:
        return self.head == -1

    def display(self):
        """
        1->3->5->6  => 6-1-3
        ^        ^
        """
        if self.head > self.tail:
            for idx in range(self.head, len(self.data)):
                print(self.data[idx], end='->')
            for idx in range(0, self.tail + 1):
                print(self.data[idx], end='->')
            print()
        elif self.head == self.tail:
            print(self.data[self.head])
        else:
            for idx in range(self.head, len(self.data)):
                print(self.data[idx], end='->')
            print()


q = CircularQueue(5)
q.enqueue(1)
q.enqueue(3)
q.enqueue(7)
q.enqueue(8)
q.enqueue(9)
q.display()
q.dequeue()
q.dequeue()
q.display()
q.enqueue(10)
q.display()
print(q.data)
"""

[10, 3, 7, 8, 9]
  ^     ^
"""
