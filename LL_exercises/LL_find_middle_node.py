class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node


    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True

# SOLUTION FROM CODECADEMY
    def find_middle_node(self):
        fast = self.head
        slow = self.head
        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
                slow = slow.next
        return slow

# OTHER SOLUTION FROM CODECADEMY
# Half-Speed
# Another equally valid solution is to move 
# the fast pointer once with each loop iteration 
# but only move the slow pointer every-other iteration:
    def find_middle_alt(linked_list):
      count = 0
      fast = linked_list.head_node
      slow = linked_list.head_node
      while fast:
        fast = fast.get_next_node()
        if count % 2 != 0:
          slow = slow.get_next_node()
        count += 1
      return slow


# SOLUTION FROM SCOTT BARRETT 
    def find_middle_node(self):
        slow = self.head
        fast = self.head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        return slow

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.append(6)

print( my_linked_list.find_middle_node().value )



"""
    EXPECTED OUTPUT:
    ----------------
    3
    
"""