class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class Queue:  
   def __init__(self):
       self.front = None
       self.rear = None
   def enqueue(self, elem):
       node = Node(elem)
       if self.front is None:
           self.front = node
           self.rear = node
       else:
           self.rear.next = node
           self.rear = node
   def dequeue(self):
       if self.front is None:
           print("Can't dequeue an empty queue")
       else:
           deq = self.front.value
           self.front = self.front.next
           if self.front is None:
               self.rear = None
           return deq
   def print(self):
       if self.front is None:
           print("There is nothing to print. Empty queue.")
       else:
           head = self.front
           while head is not None:
               print(head.value)
               head = head.next

   def delete_alternate_nodes(self):
       if self.front is None:
           print("There is nothing to be deleted.")
       elif self.front.next is None:
           self.front = None
       elif self.front.next.next is None:
           self.front.next = None
       pass

queue = Queue()
queue.dequeue()
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(12)
queue.enqueue(24)
queue.print()