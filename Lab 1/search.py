
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i

    return -1

def binary_search(data, target): 
    low = 0
    high = len(data) - 1
    mid = 0
  
    while low <= high: 
  
        mid = (high + low) // 2
  
        # Check if xtarget is present at mid 
        if data[mid] < target: 
            low = mid + 1
  
        # If target is greater, ignore left half 
        elif data[mid] > target: 
            high = mid - 1
  
        # If target is smaller, ignore right half 
        else: 
            return mid 
  
    # If we reach here, then the element was not present 
    return -1
    