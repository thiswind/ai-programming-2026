# 复利计算器（课程第一个程序：意图→上下文→生成→验证→迭代）
# FV = PV * (1 + r/n) ** (n*t)   n=每年复利次数

def compound_fv(pv, r, t, n=1):
    """复利终值：pv 本金, r 年利率, t 年限, n 每年复利次数"""
    if pv <= 0 or t <= 0:
        raise ValueError("本金与年限必须为正数")
    if r < 0:
        raise ValueError("利率不能为负")
    return pv * (1 + r / n) ** (n * t)


def simple_fv(pv, r, t):
    """单利终值"""
    return pv * (1 + r * t)


def read_positive(prompt):
    """读入正数：负数/零时提示重输（step2 参数校验）"""
    while True:
        try:
            v = float(input(prompt))
        except ValueError:
            print("请输入数字")
            continue
        if v <= 0:
            print("数值必须为正，请重输")
            continue
        return v


def read_rate(prompt):
    """读入利率：允许 0，禁止负（step2 检查点：-0.05 被拦截）"""
    while True:
        try:
            v = float(input(prompt))
        except ValueError:
            print("请输入数字")
            continue
        if v < 0:
            print("利率不能为负，请重输")
            continue
        return v


def main():
    print("=== 复利 vs 单利对比（step3 对比版） ===")
    pv = read_positive("本金（元）：")
    r = read_rate("年利率（如 0.05）：")
    print(f"{'年限':<6}{'复利终值':>12}{'单利终值':>12}{'差额':>12}")
    for t in (10, 20, 30):
        c, s = compound_fv(pv, r, t), simple_fv(pv, r, t)
        print(f"{t:<8}{c:>12.2f}{s:>12.2f}{c - s:>12.2f}")


if __name__ == "__main__":
    main()
