

class stack(object):
    
    def __init__(self):
        self.stack = []

    def push_stack(self, data):
        self.stack.append(data)

    def pop_stack(self):
        try:
            self.stack.pop()
        except:
            print("\n[*] No more elements to remove from stack")

    def print_stack(self):

        if len(self.stack) == 0:
            print("\n----- Stack empty ------")
            return
        
        print("\n------ Stack start ------")

        for i in reversed(range(0, len(self.stack))):
            print(self.stack[i])

        print("------ Stack bottom ------")


if __name__ == "__main__":
    
    print("[*] Implementation of stack using class")
    
    # Driver code
    stack = stack()
    stack.push_stack(20)
    stack.push_stack(30)
    stack.push_stack(28)
    stack.push_stack(59)
    stack.print_stack()
    stack.pop_stack()
    stack.pop_stack()
    stack.print_stack()
