# Algorithms

## 1. Selection Sort

Code snippet :

```python
def selec_sort(arr):
  
   for i in range(0, len(arr)-1):
       min = i
       for j in range(i+1, len(arr)):
           if arr[j] < arr[min]:
               min = j
       arr[min] , arr[i] = arr[i] , arr[min]
   return arr
```
Full code at :
https://github.com/AmunRha/ChallengeSet1/blob/master/Algorithms/selecSort.py

## 2. Bubble Sort

Code snippet :

```python
def bble_sort(arr):
 
   for i in range(0, len(arr)):
       for j in range(0, len(arr)-i-1):
           if arr[j] > arr[j+1]:
               arr[j] , arr [j+1] = arr[j+1] , arr[j]
   return arr
```
Full Code at :
https://github.com/AmunRha/ChallengeSet1/blob/master/Algorithms/bbleSort.py

## 3. Merge Sort

Code snippet :

```python
def merge_sort(arr):
   if len(arr) >= 2:
       # Dividing Part
       mid = int(len(arr)/2)
       a = arr[:mid]
       b = arr[mid:]
       a = merge_sort(a)
       b = merge_sort(b)
       # Merging Part
       i = j = k = 0
       while i<len(a) and j < len(b):
           if a[i] <= b[j]:
               arr[k] = a[i]
               i+=1      
           else:
               arr[k] = b[j]
               j+=1
           k+=1
       while i < len(a):
           arr[k] = a[i]
           k+=1
           i+=1
       while j < len(b):
           arr[k] = b[j]
           k+=1
           j+=1
   return arr
```
Full code at :
https://github.com/AmunRha/ChallengeSet1/blob/master/Algorithms/mergeSort.py

## 4. Binary Search

```python
def bin_srch(arr, srch_elem):
  
   start = 0
   end = len(arr)-1
   while start<=end :
       mid = int((start + end)/2)
       if srch_elem < arr[mid]:
           end = mid - 1
       elif srch_elem >  arr[mid]:
           start = mid + 1
       elif srch_elem == arr[mid]:
           return True, mid
   return False, -1
```
Full code at :
https://github.com/AmunRha/ChallengeSet1/blob/master/Algorithms/binSearch.py

## 5. Balanced Parentheses using Stack

```python
def check_balanced(inp):
   stack_1 = stack_2 = stack_3 = []
   remains = False
 
   for char in inp:
       # Only work if the entered characters are any sort of paranthsis
       if char=='(' or char==')' or char=='{' or char=='}' or char=='[' or char==']':
           if char=='(':
               stack_1.append(char)
           elif char=='{':
               stack_2.append(char)
           elif char=='[':
               stack_3.append(char)
           # Catch the exception in case there is an extra closing bracket
           try:
               if char==')':
                   stack_1.pop()
               elif char=='}':
                   stack_2.pop()
               elif char==']':
                   stack_3.pop()
           except:
               remains = True
               break
   if len(stack_1) == 0 and len(stack_2) == 0 and len(stack_3) == 0 and remains == False:
       return True
   else:
       return False
```
Full code at :
https://github.com/AmunRha/ChallengeSet1/blob/master/Algorithms/balParanStack.py

## 6. Loop in Linked List

```python
def check_loop(self):
       slow = fast = self.root
       while slow and fast and fast.next:
           slow = slow.next
           fast = fast.next.next
           if slow == fast:
               return True
       return False
```
Full code at :
https://github.com/AmunRha/ChallengeSet1/blob/master/Algorithms/cycleLnkList.py

