"""# # for question A
# # input
# # 6
# # 2 2 1
# # 1 1
# # 1 2
# # 2 2 2
# # 1 1
# # 2 2
# # 2 2
# # 1 2 1
# # 1 1
# # 1 2
# # 5 5 4
# # 3 3
# # 1 1
# # 1 5
# # 5 1
# # 5 5
# # 2 2 2
# # 1 1
# # 2 1
# # 1 2
# # 3 4 1
# # 1 2
# # 3 3
# #out put
# YES
# NO
# YES
# NO
# YES
# YES

# Note
# In the first test case, Vika can repaint the plank in the middle in color 1
#  and walk across the bridge without stepping over any planks.
#
# In the second test case, Vika can repaint the plank in the middle in color 2
#  and walk across the bridge, stepping over only one plank each time.
#
# In the third test case, Vika can repaint the penultimate plank in color 2
#  and walk across the bridge, stepping only on planks with numbers 2
#  and 5
# . Then Vika will have to step over 1
# , 2
#  and 1
#  plank each time she steps, so the answer is 2
# .
#
# In the fourth test case, Vika can simply walk across the bridge without repainting it, stepping over two planks each time, walking on planks of color 3
#
#
# In the fifth test case, Vika can simply walk across the bridge without repainting it, without stepping over any planks
# question b
# input
# 5
# 5 2
# 1 1 2 1 1
# 7 3
# 1 2 3 3 3 2 1
# 6 6
# 1 2 3 4 5 6
# 8 4
# 1 2 3 4 2 3 1 4
# 3 1
# 1 1 1
# out put
# 0
# 1
# 2
# 2
# 0
# Note
# In the first test case, Vika can repaint the plank in the middle in color 1
#  and walk across the bridge without stepping over any planks.
#
# In the second test case, Vika can repaint the plank in the middle in color 2
#  and walk across the bridge, stepping over only one plank each time.
#
# In the third test case, Vika can repaint the penultimate plank in color 2
#  and walk across the bridge, stepping only on planks with numbers 2
#  and 5
# . Then Vika will have to step over 1
# , 2
#  and 1
#  plank each time she steps, so the answer is 2
# .
#
# In the fourth test case, Vika can simply walk across the bridge without repainting it, stepping over two planks each time, walking on planks of color 3
# .
#
# In the fifth test case, Vika can simply walk across the bridge without repainting it, without stepping over any plank
# question c
# input
# 9
# 4
# 0 0 0 0
# 1 2 3 4
# 3
# 1 2 3
# 1 2 3
# 2
# 1 2
# 2 1
# 6
# 100 23 53 11 56 32
# 1245 31 12 6 6 6
# 7
# 1 2 3 4 5 6 7
# 7 6 5 4 3 2 1
# 3
# 4 0 2
# 4 0 2
# 3
# 2 5 2
# 1 3 4
# 2
# 6 1
# 4 2
# 2
# 0 0
# 0 3
# out put
# YES
# YES
# NO
# NO
# YES
# YES
# NO
# YES
# YES
# Note
# In the first test case, the array a
#  is initially zero.
#
# In the second test case, after the first operation a=[1,2,3],b=[0,0,0]
# . After the second operation a=[0,0,0],b=[1,2,3]
# .
#
# In the third test case, it can be shown that the array a
#  will never become zero
# question D
# input
# 6
# 1 3
# 11 3
# 0 179
# 5 1000000000
# 723252212 856168102
# 728598293 145725253
# out put
# 4
# 33
# 0
# 9999999990
# 1252047198518668448
# 106175170582793129
# Note
# In the first test case, Vika can accumulate bonuses after the first and second purchases, after which she can get a discount of 4
# .
#
# In the second test case, Vika can get a discount of 11
#  three times, and the total discount will be 33
# .
#
# In the third example, regardless of Vikas actions, she will always get a total discount of 0
# .
#question E
# input
# 1 2 179
# 2 3
# # output
# 1
# 2
# input
# 7 5 998244353
# 2 13 1 44 179
# out put
# 2
# 4
# 4
# 8
# 16
# input
# 1000000000 10 179
# 58989 49494 8799 9794 97414 141241 552545 145555 548959 774175
# out put
# 120
# 4
# 16
# 64
# 111
# 43
# 150
# 85
# 161
# 95
# Note
# In the first sample, to make the stone touch the water at a point with coordinate 2
# , it needs to be thrown with a force of 2
# . To make the stone touch the water at a point with coordinate 2⋅3=6
# , it needs to be thrown with a force of 3
#  or 6
# .
#
# In the second sample, you can skim a stone with a force of 5
#  or 14
#  to make it touch the water at a point with coordinate 7⋅2=14
# . For the coordinate 14⋅13=182
# , there are 4
#  possible forces: 20
# , 29, 47,  182
# question F
#input
# 4
# 1 2 1 2
#out put
# 2
# input
# 2
# 0 0
# out put
# 0
# input
# 1
# 14
# out put
# 1
# input
# 8
# 0 1 2 3 4 5 6 7
# 5
# Note
# In the first example, after one operation, the array a
#  will become equal to [3,3,3,3]
# . After one more operation, it will become equal to [0,0,0,0]
# .
#
# In the second example, the array a
#  initially consists only of zeros.
#
# In the third example, after one operation, the array a
#  will become equal to [0]
# .
"""
