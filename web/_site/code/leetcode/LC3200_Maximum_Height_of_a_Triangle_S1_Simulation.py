class Solution:
	def maxHeightOfTriangle(self, red: int, blue: int) -> int:
		def f(red: int, blue: int) -> int:
			# 1, 3, 5奇数排放red
			# 0, 2, 4偶数排放blue
			left = [blue, red]
			i = 1  # 第i行，应该放置i个球
			while left[i % 2] >= i:
				left[i % 2] -= i
				i += 1
			return i - 1    # i-1是因为在while循环中：i+1之后的那一排不满足条件跳出了while循环。
		return max(f(red, blue), f(blue, red))