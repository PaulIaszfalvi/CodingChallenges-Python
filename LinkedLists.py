import random
class LinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node is not None:
            yield node
            node = node.next

    def __repr__(self):
        nodes = []
        for node in self:
            nodes.append(node.val)
        return " -> ".join(nodes)

    def add_to_tail(self, node):
        if self.head == None:
            self.head = node
            return
        for current_node in self:
            pass
        current_node.set_next(node)

    def remove_from_head(self):
        if self.head == None:
            return None
        temp = self.head
        self.head = self.head.next
        return temp

    def reverse(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

      # This function mainly calls reverseUtil()
    # with previous as None

    def reverseUtil(self, curr, prev):
     
        # If last node mark it head
        if curr.next is None:
            self.head = curr
 
            # Update next to prev node
            curr.next = prev
            return
 
        # Save curr.next node for recursive call
        next = curr.next
 
        # And update next
        curr.next = prev
 
        self.reverseUtil(next, curr)
 
    def recursive_reverse(self):
        if self.head is None:
            return
        self.reverseUtil(self.head, None)
 
    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
 
    # Utility function to print the linked LinkedList
    def printList(self):
        temp = self.head
        myList = []
        while(temp):
            myList.append(temp.val)
            temp = temp.next
        print(myList)
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def set_next(self, node):
        self.next = node

    def __repr__(self):
        return self.val

# linked_list = LinkedList()
# for j in range(2):
#     for i in range(20):
#         linked_list.add_to_tail(Node(str(i)))
# linked_list.add_to_tail(Node('john'))
# linked_list.add_to_tail(Node('sally'))
# linked_list.add_to_tail(Node('jimmy'))

# print("ll:", linked_list)
# first = linked_list.remove_from_head()
# print("removed:", first)
# print("ll:", linked_list)

link_list = LinkedList()

string = "racecaR"

for i in string[::]:
    link_list.add_to_tail(Node(i))

link_list.printList()
link_list.recursive_reverse()
link_list.printList()

print(link_list == 
link_list.reverse())
print(link_list)