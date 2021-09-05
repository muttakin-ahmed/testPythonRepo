import Queue_implementation_with_node_class

class Stack_with_queue:
    def __init__(self) -> None:
        self.q1 = Queue_implementation_with_node_class.Queue()
        self.q2 = Queue_implementation_with_node_class.Queue()

    def pop(self):
        if self.isEmpty(self.q1) == False:
            x = self.q1.dequeue()
            return x
        return None

    def push(self, elem):
        while self.isEmpty(self.q1) == False:
            x = self.q1.dequeue()
            self.q2.enqueue(x)
        self.q1.enqueue(elem)
        while self.isEmpty(self.q2):
            x = self.q2.dequeue()
            self.q1.enqueue(x)

    def isEmpty(self, q):
        return self.q.front == None

