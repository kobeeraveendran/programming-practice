class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:

    def __init__(self, value):
        self.head = Node(value)
    
    def append(self, value):

        curr = self.head

        while curr.next != None:
            curr = curr.next

        curr.next = Node(value)

    def printList(self):
        curr = self.head

        while curr != None:
            print(str(curr.value) + ' -->', end = ' ')
            curr = curr.next

        print('None')

    def removeDuplicates(self):
        seen = set()

        curr = self.head

        while curr.next != None:
            if curr.next.value in seen:
                curr.next = curr.next.next

            else:
                seen.add(curr.next.value)

            curr = curr.next

head = LinkedList(1)
head.append(2)
head.append(2)
head.append(5)
head.append(1)

head.printList()

head.removeDuplicates()

head.printList()