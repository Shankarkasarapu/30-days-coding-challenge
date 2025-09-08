class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
class MyLinkedList:

    def __init__(self):
        self.head=None
        self.size=0
    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current = self.head
        for _ in range(index):
            current = current.next
        return current.data

    def addAtHead(self, val: int) -> None:
        n=Node(val)
        n.next =self.head
        self.head = n       
        self.size+=1

    def addAtTail(self, val: int) -> None:
        n=Node(val)
        if not self.head :
            self.head=n
        else :
            temp=self.head
            while temp.next:
                temp=temp.next 
            temp.next = n
        self.size+=1
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return

        current = self.head
        new_node = Node(val)

        if index <= 0:
            new_node.next = current
            self.head = new_node
        else:
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node

        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index-1):
                current = current.next
            current.next = current.next.next
        self.size -= 1
            


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)