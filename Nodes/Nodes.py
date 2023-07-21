# Create the Node class below:
class Node:
  def __init__(self, value, link_node=None):
    self.value = value
    self.link_node = link_node

  def get_value(self):
    return self.value

  def set_next_node(self, link_node):
    self.link_node = link_node
    
  def get_next_node(self):
    return hex(id(self.link_node))

a = Node(5)
b = Node(10, a)
c = Node(20, b)
d = Node(30, a)

values = [a, b, c, d]

for value in values:
  print(value.get_value(), value.get_next_node())