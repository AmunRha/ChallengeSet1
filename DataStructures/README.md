# Data Structures

## 1. Linked List

Code snippet :

```python
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
   def remove(self, data):
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
```
Full code at :
https://github.com/AmunRha/ChallengeSet1/blob/master/DataStructures/lnkList.py

## 2. Doubly Linked List

Code snippet :

```python
class node(object):
   def __init__(self, data, n1 = None, n2 = None):
       self.data = data
       self.next = n1
       self.prev = n2
 
class linked_list(object):
   def __init__(self):
       self.root = None
   def add_beg(self, data):
       new_node = node(data, self.root)
       if self.root is not None:
           self.root.prev = new_node
       self.root = new_node
   def remove(self, data):
       temp = self.root
       found = False
       while temp.next:
           if temp.data == data:
               found = True
               break
           temp = temp.next
       if found == True:
           temp.next.prev = temp.prev
           temp.prev.next = temp.next
           temp = None
           print("\n[*] Node successfully removed")
       elif found == False:
           print("\n[*] Given data not found in Linked List")
```
Full code at :
https://github.com/AmunRha/ChallengeSet1/blob/master/DataStructures/doublyLnkList.py

## 3. Circular Linked List

Code snippet :

```python
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
   def remove(self, data):
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
```
Full code at :
https://github.com/AmunRha/ChallengeSet1/blob/master/DataStructures/cirLnkList.py

## 4. Stack 

Code snippet :

```python
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
```
Full code at :
https://github.com/AmunRha/ChallengeSet1/blob/master/DataStructures/stack.py

## 5. Queue

Code snippet :

```python
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
```
Full code at :
https://github.com/AmunRha/ChallengeSet1/blob/master/DataStructures/queue.py

## 6. Double Ended Queue

Code snippet :

```python
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
```
Full code at :
https://github.com/AmunRha/ChallengeSet1/blob/master/DataStructures/dequeue.py
