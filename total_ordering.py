# 思路：
# 1. 确定起始位置
# 2. 对之后的位置元素进行全排列
# 3. 递归进行，需要回溯，不打乱原始状态

def total_ordering(listin, start_pos):
    if start_pos>=len(listin): print(listin)
    for i in range(start_pos, len(listin)):
        # 确定起始位置，一开始i为start_pos，实质上不交换
        swap(listin, start_pos, i)
        # 对之后位置进行全排列
        total_ordering(listin, start_pos+1)
        # 进行回溯，不打乱原始状态
        swap(listin, start_pos, i)

def swap(listin, i, j):
    listin[i], listin[j] = listin[j], listin[i]
    return listin

if __name__ == "__main__":
    listin = [1, 2, 3, 4]
    print("Initial list:", listin)
    print("After ordering:")
    total_ordering(listin, 0)