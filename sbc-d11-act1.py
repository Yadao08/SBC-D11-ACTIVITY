
def bubble_sort(array):
    length = len(array)     # Determine the length of the input list
    step = 1
    for pass_num in range(length):      # Outer loop for each pass through the list
        print(f"Pass {pass_num + 1}:")
        swapped = False     # Keep track if any swaps are made during this pass
        for index in range(0, length - pass_num - 1):   # Inner loop to compare adjacent elements
            print(f"  Step {step}: {array}", end=" -> ")
            # Compare the current element with the next one
            if array[index] > array[index + 1]:
                array[index], array[index + 1] = array[index + 1], array[index]
                swapped = True  # Mark that a swap was made
                print(f"swapped: {array}")
            else:
                print("no swap")
            step += 1       # Increment the step counter
        if not swapped:
            break
        print(f"End of pass {pass_num + 1}: {array}\n")
    return array    # Return the sorted list

# Predefined list to sort
unsorted_list = ['Q', 'S', 'A', 'M', 'Z', 'R']

# Sort the list using bubble sort
sorted_list = bubble_sort(unsorted_list)

# Print the final sorted list
print("Sorted array is:", sorted_list)
