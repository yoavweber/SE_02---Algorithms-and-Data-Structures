
class Queue:
    def __init__(self):
        self.queue = []

    def __name__(self):
        return 'test'

    def isEmpty(self):
        return self.queue == []

    def add(self,data):
        self.queue.append(data)
    
    def pop(self):
        data = self.queue[0]
        del self.queue[0]
        return data
    
    def peek(self):
        return self.queue[0]

    def sizeQueue(self):
        return len(self.queue)

    def inQueue(self,data):
        for i in self.queue:
            if i == data:
                return True
        return False

