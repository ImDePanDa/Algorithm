def merge(A, B):
    length_a, length_b = len(A), len(B)
    i, j, res = 0, 0, []
    while i < length_a and j < length_b:
        if A[i] < B[j]: 
            res.append(A[i])
            i += 1
        else:
            res.append(B[j])
            j += 1
    if i == length_a:
        for val in B[j:]:
            res.append(val)
    else:
        for val in A[i:]:
            res.append(val)
    return res 

def merge_sort(input_list):
    length = len(input_list)
    if length <= 1: return input_list
    left = merge_sort(input_list[:length//2])
    right = merge_sort(input_list[length//2:])
    return merge(left, right)     

if __name__ == "__main__":
    input_list = [9, 10, 7, 3, 6, 18, 5, 4, 3, 11]
    input_list = merge_sort(input_list)
    print(input_list)