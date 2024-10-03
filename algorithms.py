import random as rand

# ======= bubble sort algorithm ======
def bubbleSort(container):

    for i in container:
        temp = 0
        # ===== this is the loop that does the swapping ==== 
        for j in range(i + 1,len(container) -1): 
            if i > container[j] :
                temp = i 
                i = container[j]
                container[j] = temp 

    return container 
                     
# ===== insertion sort algorithm =====
def insertionSort(container):
    length = len(container)
    
    if length <= 1:
        return
    
    for i in range(1,length):
        k = container[i]
        j = i-1
        while j >= 0 and k < container[j]:
            container[j+1] = container[j]
            j = j-1
        container[j+1] = k

# ===== merge sort algorithm ===== 
def merge(left, right):
    sortedList = []
    i = 0
    j = 0
    while ( i < len(left) and j < len(right)):
        if(left[i] < right[j]):
            sortedList.append(left[i])
            i += 1
        
        elif(right[j] <= left[i]):
            sortedList.append(right[j])
            j += 1
     
    
    sortedList.extend(left[i: ])
    sortedList.extend(right[j: ])

    return sortedList


def mergeSort(container):
    baseCaseVal = len(container)

    if baseCaseVal == 1:
        return container
    else : 
        midpoint = baseCaseVal // 2

        left = mergeSort(container[: midpoint])
        right = mergeSort(container[midpoint:])

    return merge(left, right)

# ====== quick sort algorithm ====== 
def partition(array, low, high):

    mid = (low + high) // 2
 
    if(array[low] > array[mid]):
        array[low], array[mid] = array[low], array[mid]

    if(array[low] > array[high]):
        array[low], array[high] = array[high], array[low]
 
    if(array[mid] > array[high]):
        array[mid], array[high] = array[high], array[mid]
    
    array[mid], array[low] = array[low], array[mid]

    pivot = array[low]

    i = low  +1
    j = high

    while(i <= j):
        if (array[j] < pivot and array[i] > pivot and i < j):
            array[j], array[i] = array[i], array[j]
        
        if(pivot >= array[i]):
            i+= 1
        if (pivot <= array[j]):
            j -= 1

    array[low], array[j] = array[j], array[low]
            
    return j

def quickSort(a, low , high):
    
    if(low < high):
    
        pivotIndex = partition(a, low, high)
        quickSort(a, low, pivotIndex - 1)
        quickSort(a, pivotIndex + 1, high)
    
    return a

# ======== helper methods =======
     
def genNums(startRange = 1, endRange = 100, generatedNums = 15):
    
    numbersToBeSorted = []
    for  i in range(0, generatedNums):
        aNumber = rand.randint(startRange, endRange)
        numbersToBeSorted.append(aNumber)

    return numbersToBeSorted

def printResults(unsortedList, sortedList, algorithmUsed):
    print(f"the algorithm used was {algorithmUsed}")
    print (f"the unsorted list is :: {unsortedList}")
    print (f"the sorted list is :: {sortedList} " )
    
    # ======= helper methods test ========
if __name__ == "__main__":
    print("this is a test for printResuts() and genNums()")
    
    generatedNumber = genNums(1, 50, 10) 
    printResults(generatedNumber, generatedNumber, "no_sort_used")
    
