import random as rand

# ======= bubble sort algorithm ======
def bubbleSort(container):

    for i in range (0, len(container)):
        temp = 0
        # ===== this is the loop that does the swapping ==== 
        for j in range(i + 1,len(container)): 
            if container[i] > container[j] :
                temp = container[i] 
                container[i] = container[j]
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

    return container

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

def quickSortDriver(array):
    return quickSort(array, 0, len(array) - 1)

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
    
    # ======= dafualt sort test ========
if __name__ == "__main__":
    print("this is in case the front end does not work for whatever reason\n\n")
    
    #
    # I had to make copies of each array because the sorts directly manipulated them
    # it shouldn't be too bad since the arrays are only 15 elements long
    #
     

    # === insert
    print("insertion sort \n")
    unsortedList_insert = genNums()
    copy_insertion = unsortedList_insert.copy()
    sortedList_insert = insertionSort(copy_insertion)
    printResults(unsortedList_insert, sortedList_insert, "inertion sort")

    # === bubble
    print("\n\nbubble sort\n")
    unsortedList_bubble = genNums()
    copy_bubble = unsortedList_bubble.copy()
    sortedList_bubble = bubbleSort(copy_bubble)
    printResults(unsortedList_bubble, sortedList_bubble, "bubble sort")

    #=== merge
    print("\n\nmerge sort\n")
    unsortedList_merge = genNums()
    sortedList_merge = mergeSort(unsortedList_merge)
    printResults(unsortedList_merge, sortedList_merge, "merge sort")

    # === quick
    print("\n\nquick sort\n")
    unsortedList_quick = genNums()
    copy_quickSort = unsortedList_quick.copy()
    sortedList_quick = quickSort(copy_quickSort, 0, len(copy_quickSort) - 1)
    printResults(unsortedList_quick, sortedList_quick, "quick sort")



    
