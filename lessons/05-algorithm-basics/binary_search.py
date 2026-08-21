# 二分查找（前提：有序！故意实验：未排序传入结果不可预测）
def binary_search(rates, target):
    """rates 升序；返回下标或 None；打印比较次数"""
    lo, hi, n_cmp = 0, len(rates) - 1, 0
    while lo <= hi:
        mid = (lo + hi) // 2
        n_cmp += 1
        if rates[mid] == target:
            print(f"命中下标 {mid}，比较 {n_cmp} 次")   # 1024档应≤10次
            return mid
        if rates[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    print(f"未找到（比较 {n_cmp} 次）")
    return None


if __name__ == "__main__":
    table = [round(3.0 + i * 0.01, 2) for i in range(1024)]  # 1024 档利率表
    binary_search(table, 3.75)
