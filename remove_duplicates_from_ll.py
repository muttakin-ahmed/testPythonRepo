class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, list_of_elems) -> None:
        if len(list_of_elems) == 0:
            self.head = None
            return
        self.not_all_int = False
        if self.check_all_elems_are_int(list_of_elems) is False:
            self.not_all_int = True
        self.head = Node(list_of_elems[0])
        cur = self.head
        for x in list_of_elems[1:]:
            node = Node(x)
            cur.next = node
            if x == list_of_elems[len(list_of_elems) - 1]:
                node.next = None
            cur = cur.next
    
    def check_all_elems_are_int(self, arr):
        for x in arr:
            if type(x) != int:
                print(type(x))
                return False
        return True

    def delete_duplicate_nodes(self):
        if self.head is None:
            print("Empty Linked List.")
            return
        root = Node(0)
        root.next = self.head
        prev, cur = root, self.head
        seen = []

        while cur:
            if cur.value in seen:
                prev.next = cur.next
            else:
                prev = cur
                seen.append(cur.value)
            cur = cur.next
            #print(seen)
        self.head = root.next 
                

    def print(self) -> None:
        if self.not_all_int:
            print("All the elements should be integers for this linked list.")
            return
        if self.head is None:
            print("Empty Linked List.")
        else:
            arr = []
            cur = self.head
            while cur:
                arr.append(cur.value)
                cur = cur.next
            print(arr)

    

arr = [1, 23, 23, 112, 112, 1, 4]
ll = LinkedList(arr)
ll.delete_duplicate_nodes()
ll.print()

