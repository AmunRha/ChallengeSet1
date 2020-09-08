
class dequeue(object):

    def __init__(self):
        self.deq = []
    
    def push_front(self, data):
        self.deq.append(data)
    
    def pop_rear(self):
        try:
            self.deq.pop(0)
        except:
            print("[*] Double ended queue is empty")
        
    def push_rear(self, data):
        self.deq.insert(0, data)
    
    def pop_front(self):
        self.deq.pop()

    def print_dequeue(self):
        
        if len(self.deq) == 0:
            print("[*] Double ended queue empty")
            return
        
        print("\n------ Double ended queue Rear ------")
        
        for i in range(0, len(self.deq)):
            print(self.deq[i])

        print("------ Double ended queue Front ------")


if __name__ == "__main__":
    
    print("[*] Implementation of double ended queue using classes")

    # Driver code
    deq = dequeue()
    deq.push_front(20)
    deq.push_front(30)
    deq.push_front(40)
    deq.push_front(50)
    deq.print_dequeue()
    deq.push_rear(25)
    deq.push_rear(35)
    deq.push_rear(45)
    deq.print_dequeue()
    deq.pop_front()
    deq.pop_front()
    deq.print_dequeue()
    deq.pop_rear()
    deq.pop_rear()
    deq.print_dequeue()