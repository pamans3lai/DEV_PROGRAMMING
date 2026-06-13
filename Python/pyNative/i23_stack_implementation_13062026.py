class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return "Stack is empty"

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

    def is_empty(self):
        return len(self.items) == 0

browser_history = Stack()
browser_history.push("google.com")
browser_history.push("pynative.com")

print(f"Current Top {browser_history.peek()}")
print(f"Popped {browser_history.pop()}")
print(f"New Top {browser_history.peek()}")
