# Compute the number of comparisons, use the first element of the array as the pivot element to implement quicksort

def partition(arr, low, high):
    pivot = arr[low]
    i = low + 1
    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1

def quicksort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        comparisons = pivot_index - low
        comparisons += high - pivot_index
        comparisons += quicksort(arr, low, pivot_index - 1)
        comparisons += quicksort(arr, pivot_index + 1, high)
        return comparisons
    else:
        return 0

# Read the input file
with open('quick_sort.txt', 'r') as file:
    arr = [int(line.strip()) for line in file]

# Calculate the number of comparisons
num_comparisons = quicksort(arr, 0, len(arr) - 1)
print(num_comparisons)