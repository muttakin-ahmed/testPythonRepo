array = [1,2,4,1,3,31,3,4,2,4,2,1,4,24,5,6]

def first_last_occ_checker(arr, n):
    first = 0
    final = 0
    freq = []
    for i in range(len(array)):
        if arr[i] == n:
            freq.append(i)
    first = freq[0]
    final = freq[-1]
    return first, final

print(first_last_occ_checker(array, 31))
