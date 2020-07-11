# 思路：
# 动态规划
# 1. dp表示从0到amount的硬币置换数，初始每个coin位置为1，其余为0；
# 2. 从min(amount)处开始置换，总价为i的硬币置换数量为 置换(i-coin)硬币 的数量 + 1；
# 3. 由于有多种硬币，所以每个总价i的硬币，有n（硬币数量）种置换方式，辅助函数用于找最小置换数量。

def coins_change(amount, coins):
    dp = [0] * (amount+1)
    for coin in coins:
        dp[coin] = 1
    for i in range(min(coins), amount+1):
        if dp[i]!=0: continue
        dp[i] = find_min_num(coins, dp, i)   
    return dp[-1]

def find_min_num(coins, cur_dp, cur_amount):
    dp_index = list(map(lambda x: max(cur_amount-x, 0), coins))
    temp = map(lambda i: cur_dp[i]+1 if cur_dp[i]!=0 else float("inf"), dp_index)
    return min(temp)

if __name__ == "__main__":
    amount = 7
    coins = [2, 4, 3, 8]
    min_nums = coins_change(amount, coins)
    print(min_nums)