def sqrt_fun_(n, thre):
    '''
    小数实现
    '''
    left, right = 0, n
    while left<=right:
        mid = (left+right)/2
        if -thre<=mid**2-n<=thre: return mid
        elif mid**2<n: left = mid
        elif mid**2>n: right = mid

def sqrt_fun(n):
    '''
    整数实现
    '''
    left, right = 0, n 
    while left<=right:
        mid = (left+right)//2
        if mid**2==n: return mid
        elif mid**2>n and (mid-1)**2<n: return mid
        elif mid**2>n: right = mid
        elif mid**2<n and (mid+1)**2>n: return mid
        elif mid**2<n: left = mid+1


if __name__ == "__main__":
    res1 = sqrt_fun_(1000, 0.000001)
    res2 = sqrt_fun(1000)
    print(res1, res2)