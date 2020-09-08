

class queue(object):

    def __init__(self):
        self.queue = []

    def push_queue(self, data):
        self.queue.append(data)

    def pop_queue(self):
        try:
            self.queue.pop(0)
        except:
            print("\n[*] Queue is empty")

    def print_queue(self):

        if len(self.queue) == 0:
            print("[*] Queue is empty")
            return
        
        print("\n------ Queue Rear ------")
        
        for i in range(0, len(self.queue)):
            print(self.queue[i])

        print("------ Queue Front ------")
    


if __name__ == "__main__":

    print("[*] Implementation of queue using class")
    
    # Driver code
    queue = queue()
    queue.push_queue(20)
    queue.push_queue(30)
    queue.push_queue(28)
    queue.push_queue(59)
    queue.print_queue()
    queue.pop_queue()
    queue.pop_queue()
    queue.print_queue()