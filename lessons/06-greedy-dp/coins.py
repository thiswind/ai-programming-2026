# Step1：贪心 vs 动规（亲眼看贪心翻车）
def coin_greedy(coins, amount):
    """每步取 ≤余额的最大面额"""
    coins = sorted(coins, reverse=True)
    count, used = 0, []
    for c in coins:
        while amount >= c:
            amount -= c; count += 1; used.append(c)
    return count if amount == 0 else -1, used


def coin_dp(coins, amount):
    """动规求最少枚数（dp[a] = 凑 a 元最少枚数）"""
    INF = float("inf")
    dp = [0] + [INF] * amount
    for a in range(1, amount + 1):
        for c in coins:
            if c <= a and dp[a - c] + 1 < dp[a]:
                dp[a] = dp[a - c] + 1
    return dp[amount] if dp[amount] < INF else -1


if __name__ == "__main__":
    coins = [1, 5, 11]
    g, used = coin_greedy(coins, 15)
    d = coin_dp(coins, 15)
    print(f"贪心: {g} 枚 {used}")   # 检查点1：5 枚 [11,1,1,1,1]
    print(f"动规: {d} 枚")          # 检查点1：3 枚（5+5+5）
