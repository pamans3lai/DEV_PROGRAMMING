from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.append(val)

    def dequeue(self):
        if len(self.buffer) == 0:
            return "Queue is empty"
        return self.buffer.popleft()

    def peek(self):
             return self.buffer[0] if self.buffer else None

ticket_line = Queue()
ticket_line.enqueue("Custormer A")
ticket_line.enqueue("Custormer B")

print(f"Serving: {ticket_line.dequeue()}")
print(f":Next in line: {ticket_line.peek()}")
