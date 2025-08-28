class MyCircularQueue(object):

    def __init__(self, k):
        self.queue = [0] * k
        self.capacity = k
        self.head = 0
        self.count = 0

    def enQueue(self, value):
        if self.count == self.capacity:
            return False
        self.queue[(self.head + self.count) % self.capacity] = value
        self.count += 1
        return True

    def deQueue(self):
        if self.count == 0:
            return False
        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self):
        if self.count == 0:
            return -1
        return self.queue[self.head]

    def Rear(self):
        if self.count == 0:
            return -1
        return self.queue[(self.head + self.count - 1) % self.capacity]

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.capacity