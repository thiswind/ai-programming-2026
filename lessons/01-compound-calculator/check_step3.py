# step3 检查点：10000 元 5%，30 年复利-单利差额约 20798
from compound_calc import compound_fv, simple_fv

diff = compound_fv(10000, 0.05, 30) - simple_fv(10000, 0.05, 30)
assert abs(diff - 18219.42) < 5, diff
print("检查点3通过: 差额 =", round(diff, 2))
