# oa = our algorithms 
import algorithms as oa

if __name__ == "__main__":
    
    print("Welcome to the test suite of selected sorting algorithms!")
    
    while True:
        print("\nSelect the sorting algorithm you want to test.")
        print("-------------------------")
        print("1. Bubble Sort")
        print("2. Merge Sort")
        print("3. Quick Sort")
        print("4. Insertion Sort")
        print("5. Exit")
        
        choice = input("Select a sorting algorithm (1-5): ")
        
        if choice == '5':
            print("Bye!")
            break
        
        algorithm_name = ""
        if choice == '1':
            algorithm_name = "Bubble Sort"
            sorting_function = bubbleSort
        elif choice == '2':
            algorithm_name = "Merge Sort"
            sorting_function = mergeSort
        elif choice == '3':
            algorithm_name = "Quick Sort"
            sorting_function = quickSort
        elif choice == '4':
            print("Insertion Sort")
            continue

        while True:
            print(f"Case Scenarios for {algorithm_name}")
            print("---------------")
            print("1. Best Case")
            print("2. Average Case")
            print("3. Worst Case")
            print("4. Exit test")
            case_choice = input("Select the case (1-4): ")
            
            if case_choice == '4':
                break

        

    # ==== TESTING BUBBLE SORT ======
        
   
    # ==== TESTING MERGE SORT======

        unsorted = oa.genNums()
        sortedList = oa.mergeSort(unsorted)
        oa.printResults(unsorted, sortedList, "merge sort")
   
    # ==== TESTING QUICK SORT ======
   
   
    # ==== TESTING ___ ======
