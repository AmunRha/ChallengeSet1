


def selec_sort(arr):
    
    for i in range(0, len(arr)-1):
        min = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min]:
                min = j
        arr[min] , arr[i] = arr[i] , arr[min]
    return arr


if __name__ == "__main__":

    print("[*] Selection Sort algorithm")
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
    sorted_arr = selec_sort(arr)
    
    print("\n\n------- The sorted arr -------")
    for i in sorted_arr:
        print(i, end = ' ')
    print()
    