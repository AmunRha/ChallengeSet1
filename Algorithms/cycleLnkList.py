

class node(object):
    
    def __init__(self, data, n = None):
        self.data = data
        self.next = n

class linkedList(object):
    
    def __init__(self):
        self.root = None

    def push(self, data):
        new_node = node(data, self.root)
        self.root = new_node

    def check_loop(self):
        slow = fast = self.root
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

if __name__ == "__main__":
    print("[*] Check if the given Linked List contains a Loop\n")

    #Insertion of list elements
    new_list = linkedList()
    new_list.push(20)
    new_list.push(4)
    new_list.push(15)
    new_list.push(10)
    new_list.push(40)

    # Pre Defined Linked List containing loop
    new_list.root.next.next.next.next.next = new_list.root

    if new_list.check_loop() == True:
        print("[*] Given Linked List contains a loop")
    else:
        print("[*] Given Linked List does not contain a loop")