
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



if __name__ == '__main__':

    print("[*] Binary Search Algorithm")
    print("[*] Enter size of the arr")
    size = int(input())
    arr = []

    print("\n[*] Enter the elements for the arr in sorted order")
    for i in range(0,size):
        inp = int(input())
        arr.append(inp)
    arr.sort()

    print("\n[*] Enter the element you want to search")
    srch_elem = int(input())
    found , idx = bin_srch(arr, srch_elem)
    
    if found == True:
        print(f'[*] Element found at index {idx}')
    elif found == False:
        print("[*] Element not found")

