#Compute the number of comparisons , using the "median-of-three" pivot rule

def median_of_three(arr, low, high):
    mid = (low + high) // 2
    candidates = [(arr[low], low), (arr[mid], mid), (arr[high], high)]
    candidates.sort()
    return candidates[1][1]

def partition(arr, low, high):
    # Find the median of three elements
    median_index = median_of_three(arr, low, high)
    # Exchange pivot (median) with the first element
    arr[low], arr[median_index] = arr[median_index], arr[low]
    
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