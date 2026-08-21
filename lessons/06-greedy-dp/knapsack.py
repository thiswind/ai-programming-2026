# Step2：0-1 背包 = 资产配置（教材第5章递推式）
def knapsack(w, v, cap):
    """至多装满版：dp[i][c] = max(不投, 投)；返回最优值与所选项目(1起)"""
    n = len(w)
    dp = [[0] * (cap + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for c in range(cap + 1):
            dp[i][c] = dp[i - 1][c]                       # 不投第 i 项
            if c >= w[i - 1]:
                dp[i][c] = max(dp[i][c],
                               dp[i - 1][c - w[i - 1]] + v[i - 1])  # 投
    # 回溯所选
    picked, c = [], cap
    for i in range(n, 0, -1):
        if dp[i][c] != dp[i - 1][c]:
            picked.append(i)
            c -= w[i - 1]
    return dp[n][cap], sorted(picked)


if __name__ == "__main__":
    w = [300, 200, 350, 400, 250]           # 项目所需资金（万）
    v = [90, 60, 115, 120, 80]              # 预期收益
    best, items = knapsack(w, v, 1000)      # 预算 1000 万
    print(f"最优收益: {best}，所选项目: {items}")
