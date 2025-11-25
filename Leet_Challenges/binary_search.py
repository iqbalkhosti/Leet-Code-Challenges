

def binary_search(arr, target):

    arr_size = len(arr)

    left = 0
    right = arr_size -1
    while (left <= right):
        mid = (left+right)//2  
 
        if (arr[mid]==target):  
            return True  
 
        if (arr[mid]>target): 
            right = mid -1  
        else:  
            left = mid+1 
          
     
    return False
 
 
 
arr = [1,2,3, 5,7,10]

print(binary_search(arr,1))
print(binary_search(arr,10))
print(binary_search(arr, 100))
print(binary_search(arr, 9))
print(binary_search(arr, 0))
