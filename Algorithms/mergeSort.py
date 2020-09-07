


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


if __name__ == "__main__":

    print("[*] Merge Sort algorithm")
    print("[*] Enter size of the arr")
    size = int(input())
    arr = []

    print("\n[*] Enter the elements in the arr")
    for i in range(0,size):
        inp = int(input())
        arr.append(inp)

    print("\n------- The unsorted arr -------")
    for i in arr:
        print(i, end = ' ')
    sorted_arr = merge_sort(arr)
    
    print("\n\n------- The sorted arr -------")
    for i in sorted_arr:
        print(i, end = ' ')
    print()