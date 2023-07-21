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
    return (self.link_node)

# Add your code below:
yacko = Node("likes to yak")
wacko = Node("has a penchant for hoarding snacks")
dot = Node("enjoys spending time in movie lots")

yacko.set_next_node(dot)
dot.set_next_node(wacko)

dots_data = yacko.get_next_node().get_next_node().get_value()
wackos_data = dot.get_value()
print(dots_data) 
print(wackos_data)