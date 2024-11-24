def count(a):
    if len(a) <= 1:
        return a, 0
    
    m = len(a) // 2

    #count 1st half of A
    firstHalf, inversion1 = count(a[:m])

    #count 2nd half of A
    secondHalf, inversion2 = count(a[m:])
    merged, split_inv = merge_and_count_split_inversions(firstHalf, secondHalf)
    
    return merged, inversion1 + inversion2 + split_inv

def merge_and_count_split_inversions(firstHalf, secondHalf):
    sortedA = []
    inversion = 0
    i, j = 0, 0
    
    while i < len(firstHalf) and j < len(secondHalf):
        if firstHalf[i] <= secondHalf[j]:
            sortedA.append(firstHalf[i])
            i += 1
        else:
            sortedA.append(secondHalf[j])
            j += 1
            inversion += len(firstHalf) - i
    
    sortedA.extend(firstHalf[i:])
    sortedA.extend(secondHalf[j:])
    
    return sortedA, inversion

def read_file(filename):
    with open(filename, 'r') as file:
        arr = [int(line.strip()) for line in file]
    
    _, inversions = count(arr)
    return inversions

filename = 'integer_array.txt'
inversions = read_file(filename)
print("Number of inversions:", inversions)