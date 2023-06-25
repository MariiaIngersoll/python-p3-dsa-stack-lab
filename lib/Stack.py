class Stack:

    def __init__(self, items = [], limit = 100):
        self.limit = limit
        self.items = items

    def isEmpty(self):
        if len(self.items) == 0:
            return True
        else:
            return False

    def push(self, item):
        if len(self.items) >= self.limit:
            raise ValueError("Stack is full")
        else:
            self.items.append(item)

    def pop(self):
        pass

    def peek(self):
        pass
    
    def size(self):
        return len(self.items)

    def full(self):
        if len(self.items) >= self.limit:
            return True
        else: 
            return False

    def search(self, target):
        if self.isEmpty():
            return -1
        
        i = len(self.items) - 1
        distance = 0

        while i >= 0:
            if self.items[i] == target:
                return distance
            i -= 1
            distance += 1

        return -1

