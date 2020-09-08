

class node(object):

    def __init__(self, data, n = None):
        self.data = data
        self.next = n

class linked_list(object):

    def __init__(self):
        self.root = None

    def add(self, data):

        new_node = node(data)
        if self.root is None:
            new_node.next = new_node
            self.root = new_node
        else:
            new_node.next = self.root
            temp = self.root
            while temp.next is not self.root:
                temp = temp.next
            temp.next = new_node
            self.root = new_node
        
    def add_bet(self, data, mid_mode):

        new_node = node(data, mid_mode.next)
        mid_mode.next = new_node

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
        while temp.next is not self.root:
            if temp.data == data:
                found = True    
                break
            prev = temp 
            temp = temp.next

        if found == False:
            print("\n[*] Given data is not in the Linked List")
        elif found == True:
            prev.next = temp.next
            temp = None
            print("\n[*] Node successfully removed")

    def print_list(self):

        if self.root is None:
            print("\n[*] Linked List is empty")
            return

        print("\n------ Linked List End ------")
        temp = self.root
        while temp.next is not self.root:
            print(temp.data)
            temp = temp.next
            if temp.next is self.root:
                print(temp.data)
        print("------ Linked List Start ------")
        



if __name__ == '__main__':
    
    print("[*] Implementation of Circular Linked List using classes")
    
    # Driver code
    llist = linked_list()
    llist.add(10)
    llist.add(20)
    llist.add(30)
    llist.add(40)
    llist.print_list()
    llist.add_bet(25, llist.root.next.next)
    llist.add_bet(35,llist.root.next)
    llist.print_list()
    llist.add(50)
    llist.add(60)
    llist.print_list()
    llist.remove(35)
    llist.print_list()
    llist.remove(70)
    llist.print_list()
    