

def bble_sort(arr):

    for i in range(0, len(arr)):
        for j in range(0, len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j] , arr [j+1] = arr[j+1] , arr[j]
    return arr


if __name__ == "__main__":

    print("[*] Bubble Sort algorithm")
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
    sorted_arr = bble_sort(arr)
    
    print("\n\n------- The sorted arr -------")
    for i in sorted_arr:
        print(i, end = ' ')
    print()