# oa = our algorithms 
import algorithms as oa

# ===== Main Test Suite =====
# still working on main

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
        sorting_function = None

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
            algorithm_name = "Insertion Sort"
            sorting_function = insertionSort
        else:
            print("Invalid choice. Please try again.")
            continue

        while True:
            print(f"\nCase Scenarios for {algorithm_name}")
            print("---------------")
            print("1. Best Case")
            print("2. Average Case")
            print("3. Worst Case")
            print("4. Exit test")
            case_choice = input("Select the case (1-4): ")

            if case_choice == '4':
                break

            given_n = [100, 1000, 10000]
            for n in given_n:
                if case_choice == '1':  # best case scenario
                    test_data = sorted(genNums(generatedNums=n))
                    print(f"In best case,")
                elif case_choice == '2':  # average case scenario
                    test_data = genNums(generatedNums=n)
                    print(f"In average case,")
                elif case_choice == '3':  # worst case scenario
                    test_data = sorted(genNums(generatedNums=n), reverse=True)
                    print(f"In worst case,")
                else:
                    print("Invalid case choice. Please try again.")
                    continue

                time_taken = measureTime(sorting_function, test_data)
                print(f"For N = {n}, it takes {time_taken:.6f} seconds")

            another_n = input("Do you want to input another N (Y/N)? ").strip().upper()
            if another_n == 'Y':
                n = int(input("What is the N? "))
                if case_choice == '1':  # best case scenario
                    test_data = sorted(genNums(generatedNums=n))
                    print(f"In best case,")
                elif case_choice == '2':  # Average case scenario
                    test_data = genNums(generatedNums=n)
                    print(f"In average case,")
                elif case_choice == '3':  # Worst case scenario
                    test_data = sorted(genNums(generatedNums=n), reverse=True)
                    print(f"In worst case,")

                time_taken = measureTime(sorting_function, test_data)
                print(f"For N = {n}, it takes {time_taken:.6f} seconds")
            else:
                break

        

    # ==== TESTING BUBBLE SORT ======
        
   
    # ==== TESTING MERGE SORT======

        unsorted = oa.genNums()
        sortedList = oa.mergeSort(unsorted)
        oa.printResults(unsorted, sortedList, "merge sort")
   
    # ==== TESTING QUICK SORT ======
   
   
    # ==== TESTING ___ ======
