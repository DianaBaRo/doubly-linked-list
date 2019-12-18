# Doubly linked lists are composed of nodes and references pointing from one node to the other.
# The last and first references are pointing to a NULL.
# We can access the first and the last nodes.

#A single node has the data and two references pointing to the next node and to the previous node.
# Because in this kind of lists we have a reference to the previous node we don't need to iterate through the list like we had to do in the single linked list.
# We can do remove operation in O(1) running time because we can access the previous node with the reference.

#Source code for remove operation in a doubly linked list:

removeDouble(Node node)

    node.previousNode.nextNode = node.nextNode
    node.nextNode.previousNode = node.previousNode

# Advantages:
  # a doubly linked list can be traverse both directions: forward and backward

#Linked List Application
  # they are important in low level memory management. Heap management.
  # applications in Windows
  # Photo viewers, where they have access to previous and next images