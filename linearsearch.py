# Linear Search

'''def linersearch(array,n,x):
    for i in range(0,n):
        if (array[i]==x):
            return i
    return -1

array = [2,4,0,1,9]
x = 1                                                  
n = len(array)
result = linersearch(array,n,x)
if(result ==-1):
    print("Element Not Found")
else:
    print("Element Found at Index: ",result)'''

# Example 1

'''def linersearch(array,n,x):
    count = 0
    for i in range(0,n):
        if (array[i]==x):
            count  = count + 1
    return count

array = [2,5,5,5,6,6,8,9,9,9]
x = int(input("Enter The Target Value: "))                                                 
n = len(array)
result = linersearch(array,n,x)
if(result == -1):
    print("Element Not Found")
else:
    print("Target has Occured: ",result," Times")'''

# Example 2 Peak Element
def findPeak(arr, n) :
 
    # first or last element is peak element
    if (n == 1) :
      return 0
    if (arr[0] >= arr[1]) :
        return 0
    if (arr[n - 1] >= arr[n - 2]) :
        return n - 1
  
    # check for every other element
    for i in range(1, n - 1) :
  
        # check if the neighbors are smaller
        if (arr[i] >= arr[i - 1] and arr[i] >= arr[i + 1]) :
            return i
             
# Driver code.
arr = [ 1, 3, 20, 4, 1, 0 ]
n = len(arr)
print("Index of a peak point is", findPeak(arr, n))
 

    