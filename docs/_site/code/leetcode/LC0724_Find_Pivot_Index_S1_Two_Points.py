from typing import List


class Solution:
	def pivotIndex(self, nums: List[int]) -> int:
		N = len(nums)
		l, r = 0, N-1
		sum_l, sum_r = 0, 0
		while l < r:
			if sum_l < sum_r:
				sum_l += nums[l]
				l += 1
			else:
				sum_r += nums[r]
				r -= 1
			print(sum_l, sum_r, l, r)
		if sum_l == sum_r:
			return l
		else:
			return -1
