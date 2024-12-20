import math
class Solution:
	def maxHeightOfTriangle(self, red: int, blue: int) -> int:
		def f(o, e):
			o = math.floor(math.sqrt(o))
			e = math.floor((math.sqrt(4*e+1) - 1)//2)
			if o>e: # 奇数行大于偶数行，最终结果由偶数行决定
				return 2*e+1
			else: # 奇数行等于或小于偶数行，最终结果由奇数行决定
				return 2*o
		return max(f(red, blue), f(blue, red))