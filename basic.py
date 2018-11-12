# 问题一：字符串排序

s = "hello world"
new_s = ''.join((lambda x: (x.sort(), x)[1])(list(s)))

# 请编写代码，将 s 以 [a-z] 顺序输出

# 问题二：数值比较

n = [9, 15, 23, 89, 33, 26, 2, 76]
n_max = max(n)
n_min = min(n)

# 请编写代码，找出数组中的最大数与最小数

# 问题三：替换

a = "i,am,a,student,in,chengdu"

# 请编写代码，将 “student” 和 “chengdu” 变为可基于参数输入配置的输出
# 通过参数输入打印出完整的句子
new_a = 'i,am,a,%s,in,%s' % ('student', 'chengdu')
