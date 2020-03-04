# 需要用到的知识点：
# 1.堆的索引： 根节点为1， 依次下去2，3，4...
# 2.索引为i的节点，左节点索引为2i, 右节点索引为2i+1.
# 3.列表length为n，则最开始有叶节点的节点，索引为n//2.

# 第一步：对于有叶节点的父节点，逐个进行基本堆检验
# 第二步：若符合则进行下一个，若不符合，则进行下沉，下沉后进行相应节点的检查
def bulid_heap(listin, start, end):
    '''
    构建堆
    '''
    size = end-start
    # 确定起始带叶节点的节点
    rootindex = size//2
    # 逐个进行基本堆检查，修改
    for i in range(rootindex, 0, -1):
        build_basic_heap(listin, size, i)

def build_basic_heap(listin, size, rootindex):
    '''
    构建基本堆
    '''
    leftchildindex = rootindex*2
    rightchildindex = rootindex*2+1
    if leftchildindex<=size:
        if listin[rootindex-1]>listin[leftchildindex-1]:
            listin[rootindex-1], listin[leftchildindex-1] = listin[leftchildindex-1], listin[rootindex-1]
            build_basic_heap(listin, size, leftchildindex)

    if rightchildindex<=size:
        if listin[rootindex-1]>listin[rightchildindex-1]:
            listin[rootindex-1], listin[rightchildindex-1] = listin[rightchildindex-1], listin[rootindex-1]
            build_basic_heap(listin, size, rightchildindex)

def heap_sort(listin):
    bulid_heap(listin, 0, len(listin))
    print("Initial build:", listin)
    for i in range(len(listin)-1, 0, -1):
        listin[0], listin[i] = listin[i], listin[0]
        print("After swap:", listin)
        # 时间复杂度为log(n)，因为只需要考虑顶的下沉
        bulid_heap(listin, 0, i)
        print("After build:", listin)

if __name__ == "__main__":
    import random
    listin = [i for i in range(9, 100, 3)]
    random.shuffle(listin)
    heap_sort(listin)
