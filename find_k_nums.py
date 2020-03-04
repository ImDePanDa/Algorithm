# 法一： 直接用快排进行排序，利用索引取得k个最大值
def quicksort(nums, left, right):
    if left>=right: return 
    i, j = left, right
    nums[i], nums[(i+j)//2] = nums[(i+j)//2], nums[i]
    target = nums[i]
    while i<j:
        while i<j and nums[j]>=target:
            j -= 1
        nums[i] = nums[j]
        while i<j and nums[i]<target:
            i += 1
        nums[j] = nums[i]
    nums[i] = target
    quicksort(nums, left, i)
    quicksort(nums, i+1, right)

# 法二： 利用快排思想逐步进行快排，定位k
#       找k最大，就是找第len(nums)+1-k小值
def main(nums, k):
    left, right = 0, len(nums)-1
    nums, index = partition(nums, left, right)
    while True:
        if index+1 == len(nums)+1-k: return nums[index]
        elif index+1<len(nums)+1-k: left = index+1
        elif index+1>len(nums)+1-k: right = index-1
        nums, index = partition(nums, left, right)

def partition(nums, left, right):
    i, j = left, right
    nums[i], nums[(i+j)//2] = nums[(i+j)//2], nums[i]
    target = nums[i]
    while i<j:
        while i<j and nums[j]>=target:
            j -= 1
        nums[i] = nums[j]
        while i<j and nums[i]<target:
            i += 1
        nums[j] = nums[i]
    nums[i] = target
    return nums, i


if __name__ == "__main__":
    nums = [3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6]
    k = 4
    # print(nums[-k])
    print(main(nums, k))