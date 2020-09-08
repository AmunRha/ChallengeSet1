
class node(object):

    def __init__(self, data, n = None):
        self.data = data
        self.next = n

class linked_list(object):

    def __init__(self):
        self.root = None
    
    def add_beg(self, data):
        new_node = node(data, self.root)
        self.root = new_node

    def add_end(self, data):

        if self.root is None:
            self.add_beg(data)
        new_node = node(data)
        temp = self.root
        while temp.next:
            temp = temp.next

        temp.next = new_node
    
    def add_bet(self, data, mid_node):

        if mid_node is None:
            return
        new_node = node(data, mid_node.next)
        mid_node.next = new_node

    def remove(self, data):

        if self.root is None:
            print("\n[*] Node is empty")
            return
        if self.root.data == data:
            self.root = None
            print("\n[*] Node successfully removed")
            return
        temp = prev = self.root
        found = False
        while temp.next:
            if temp.data == data:
                found = True
                break
            prev = temp
            temp = temp.next

        if found == False:
            print("\n[*] Given data not found in Linked List")
        else:
            prev.next = temp.next
            temp = None
            print("\n[*] Node successfully removed")

    def print_list(self):

        if self.root is None:
            print("\n[*] Linked List is empty")
            return

        print("\n------ Linked List End ------")
        temp = self.root
        while temp:
            print(temp.data)
            temp = temp.next
        print("------ Linked List Start ------")



if __name__ == '__main__':
    
    print("[*] Implementation of Linked List using classes")

    # Driver code
    llist = linked_list()
    llist.add_beg(10)
    llist.add_beg(20)
    llist.add_beg(30)
    llist.add_beg(40)
    llist.print_list()
    llist.add_bet(25, llist.root.next.next)
    llist.add_bet(35,llist.root.next)
    llist.print_list()
    llist.add_end(50)
    llist.add_end(60)
    llist.print_list()
    llist.remove(35)
    llist.print_list()
    llist.remove(70)
    llist.print_list()
    