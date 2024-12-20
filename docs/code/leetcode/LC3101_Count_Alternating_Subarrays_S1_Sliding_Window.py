from typing import List


class Solution:
	def countAlternatingSubarrays(self, nums: List[int]) -> int:
		N = len(nums)
		if N==1:
			return 1
		l, r = 0, 1
		res = N
		while r<N:
			if nums[r]!=nums[l]:
				while r+1<N and nums[r+1]!=nums[r]:
					r+=1
				res += (r-l+1)*(r-l)//2
				l = r
			else:
				l += 1
			r += 1
		return res