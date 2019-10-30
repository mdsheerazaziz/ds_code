class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
    def push_front(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
    def print_list(self):
        node = self.head
        while(node):
            print(node.data, end=',')
            node = node.next

if __name__ == '__main__':
    llist = LinkedList()
    llist.head = Node(1)
    llist.push_front(2)
    
    llist.print_list()
