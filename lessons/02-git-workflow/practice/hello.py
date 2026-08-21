# D2：打招呼程序（先提交空函数版，再补全验证）
import datetime


def greet(name: str) -> str:
    """返回问候语（D3 将在 dev 分支加日期功能）"""
    return f"你好，{name}！欢迎来到人工智能程序设计与实践。"


if __name__ == "__main__":
    print(greet("ynu"))
    print("当前日期:", datetime.date.today())  # D3 dev 分支新增
