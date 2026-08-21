# 自主实践②：打印已安装包（pip list 的 Python 版）
import importlib.metadata as md

pkgs = sorted((d.metadata["Name"], d.version) for d in md.distributions() if d.metadata["Name"])
for name, ver in pkgs:
    print(f"{name:<30}{ver}")
print(f"共 {len(pkgs)} 个包")
