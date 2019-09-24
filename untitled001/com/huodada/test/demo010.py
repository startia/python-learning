# _*_ coding:UTF-8 _*_
"""
加法        +
减法        -
乘法        *
除法        /
地板除      //
取余        %
平方根      **
"""
# 用户输入数字
num1 = input("输入第一个数字：")
num2 = input("输入第二个数字：")

# 地板除
sum = float(num1) // float(num2)

# 显示计算结果
print('数字{0}和{1}之地板除结果为：{2}'.format(num1, num2, sum))
