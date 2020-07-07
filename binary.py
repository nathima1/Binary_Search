#Binary Search Algorith 

#loop that iterates through binary index
def binary_search():
    arr = []
    n= int(input("Enter how many digits you want in the array: "))

    for i in range(0, n):
        ele = int(input())

        arr.append(ele)
    x=[]
    k = int(input("Select digit from array you wish to find: "))
    x.append(k)

    low = 0
    high = len(arr)-1 
    

    while low <= high :
        mid = (low + high)//2
        
        if arr[mid] < x[0]:
            low = mid+1
        elif x[0] < arr[mid]:
            high = mid-1
        else:
            return mid
                
    return -1
    
  
    

#test array

result = binary_search()

if result != -1:
    print("found at",result)
else:
    print("invalid")


