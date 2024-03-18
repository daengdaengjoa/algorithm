class Queue:
    def __init__(self, size):
        self.queue = []
        self.size = size

    def is_full(self):
        full = False
        if len(self.queue) == self.size:
            full = True
        return full

    def is_empty(self):
        empty = False
        if len(self.queue) == 0:
            empty = True
        return empty

    def add_q(self, data):
        if self.is_full():
            print("Queue is full")
        else:
            self.queue += [data]

    def delete_q(self):
        d_q = None
        if self.is_empty():
            print("Queue is Empty")
        else:
            d_q = self.queue[0]
            self.queue = self.queue[1:]
        return d_q

    def display_q(self):
        print(self.queue)


my_queue = Queue(5)

my_queue.display_q()
print(my_queue.is_empty())
my_queue.delete_q()
my_queue.add_q(1)
print(my_queue.is_empty())
print(my_queue.is_full())
my_queue.add_q(2)
my_queue.add_q(3)
my_queue.add_q(4)
my_queue.add_q(5)
print(my_queue.is_full())
my_queue.add_q(6)
my_queue.display_q()
my_queue.delete_q()
my_queue.add_q(1)
my_queue.display_q()
