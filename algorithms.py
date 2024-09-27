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
def quickSort():
    return NULL; 

def genNums(startRange = 1, endRange = 100, generatedNums = 15):
    
    numbersToBeSorted = []
    for  i in range(0, 15):
        aNumber = rand.randint(startRange, endRange)
        numbersToBeSorted.append(aNumber)

    return numbersToBeSorted

def printResults(unsortedList, sortedList, algorithmUsed):
    print("the algorithm used was {} ", algorithmUsed)
    print ("the unsorted list is :: {}", unsortedList)
    print ("the sorted list is :: {} ", sortedList)



    
    
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
    
    
    
if __name__ == "__main__":
    print("this is the file with the logic ")
    


