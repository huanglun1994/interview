import re

# 使用 while 循环打印 1 3 5 7 9
i = 1
while i < 10:
    if i % 2 == 1:
        print(i)
    i += 1

# 编写一个函数，查找数字 6 是否在列表 l 里，如果在，输出“found”，如果不在，输出“not found”

l = [1, 5, 7, 8, 9]


def found(lst):
    if 6 in lst:
        print('found')
    else:
        print('not found')


found(l)

# 将字符串 s 拆分成两个字符串 s1、s2，其中 s1 只包含字母，转换为小写，以 [a-z] 排序，s2 只包含数值，升序排序

s = "aAsnr3id2d4b6gs7DZsf9e1AF"


def split_seq(string):
    s1 = re.findall('[a-z,A-Z]', string)
    s1.sort()
    s1 = [s.lower() for s in s1]
    s2 = re.findall('\d+', string)
    s2.sort()
    print(''.join(s1), ''.join(s2))


split_seq(s)
