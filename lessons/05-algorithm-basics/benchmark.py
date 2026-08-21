# 性能实验：O(n^2) 冒泡 vs O(nlogn) 合并 vs 内置 sorted（每档3次取均值）
import random
import timeit

from merge_sort import merge_sort


def bubble(nums):
    a = nums[:]
    for i in range(len(a)):
        for j in range(len(a) - 1 - i):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


print(f"{'n':>6}{'冒泡(ms)':>12}{'合并(ms)':>12}{'内置(ms)':>12}")
for n in (1000, 2000, 4000, 8000):
    nums = [random.randint(0, 100000) for _ in range(n)]
    t_b = timeit.timeit(lambda: bubble(nums), number=3) / 3 * 1000
    t_m = timeit.timeit(lambda: merge_sort(nums), number=3) / 3 * 1000
    t_s = timeit.timeit(lambda: sorted(nums), number=3) / 3 * 1000
    print(f"{n:>6}{t_b:>12.1f}{t_m:>12.1f}{t_s:>12.1f}")
# 检查点3：n 翻倍时 冒泡≈×4，合并≈×2
