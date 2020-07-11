
# 思路：
# 选出target，一般为首个；
# 进行遍历排序，比target大的放在后面，比target小的放在前面；
# 分别快排序。

def quick_sort(input_list, left, right):
    if len(input_list) == 1 or left>=right: return 
    target = input_list[left]
    start, end = left, right
    while start < end:
        while start < end and input_list[end] >= target:
            end -= 1
        input_list[start] = input_list[end]
        while start < end and input_list[start] < target:
            start += 1
        input_list[end] = input_list[start]
    input_list[start] = target
    quick_sort(input_list, left, start-1)
    quick_sort(input_list, start+1, right)

if __name__ == "__main__":
    input_list = [9, 10, 7, 3, 6, 18, 5, 4, 3, 11]
    left, right = 0, len(input_list)-1
    quick_sort(input_list, left, right)
    print(input_list)
        
