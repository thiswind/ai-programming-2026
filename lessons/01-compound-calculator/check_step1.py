# step1 检查点：10000 元 5% 三年年复利 = 11576.25
from compound_calc import compound_fv

fv = compound_fv(10000, 0.05, 3)
assert abs(fv - 11576.25) < 0.01, fv
print("检查点1通过: FV =", round(fv, 2))
