# class sample:
#     def __init__(self, s):
#         self.s = s
#         s = self.s

# class s:
#     sa = sample('hi')
#     def dothis(self):
#         print(self.sa.s)

# s1 = s()
# s1.dothis()

# print(bool([1,2,3]==[1,2,3]))

import datetime as d
tdy = d.datetime.today()
date = str(tdy.day)+'/'+str(tdy.month)+'/'+str(tdy.year)

print(date)