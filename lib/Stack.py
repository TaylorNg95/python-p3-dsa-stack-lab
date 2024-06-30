class Stack:

    def __init__(self, items = [], limit = 100):
        self.items = items
        self.limit = limit

    def isEmpty(self):
        return True if len(self.items) == 0 else False

    def push(self, item):
        is_full = self.full()
        if not is_full:
            self.items.append(item)
            return self.items
        else:
            return self.items

    def pop(self):
        if(len(self.items) > 0):
            last_item = self.items[len(self.items) - 1]
            self.items.pop()
            return last_item
        else:
            return None

    def peek(self):
        return self.items[len(self.items) - 1]
    
    def size(self):
        return len(self.items)

    def full(self):
        return len(self.items) >= self.limit

    def search(self, target):
        try:
            idx = self.items.index(target)
            top = len(self.items) - 1
            return top - idx
        except ValueError:
            return -1

stk = Stack([1, 2])
print(stk.peek())