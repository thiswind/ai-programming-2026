# 合并排序（分治三步：分解-解决-合并）
def merge_sort(nums):
    if len(nums) <= 1:               # 基准情形：单元素天然有序
        return nums
    mid = len(nums) // 2             # ① 分解：对半切
    left = merge_sort(nums[:mid])    # ② 解决：递归排两半
    right = merge_sort(nums[mid:])
    return _merge(left, right)       # ③ 合并：两个有序序列归并


def _merge(a, b):
    out, i, j = [], 0, 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out.append(a[i]); i += 1
        else:
            out.append(b[j]); j += 1
    out.extend(a[i:]); out.extend(b[j:])
    return out


if __name__ == "__main__":
    print(merge_sort([8, 3, 5, 1, 9, 2]))   # 检查点1：[1,2,3,5,8,9]
