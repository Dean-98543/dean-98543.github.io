from typing import List


class Solution:
	def validStrings(self, n: int) -> List[str]:
		res = []
		mask = (1 << n) - 1
		for i in range(1 << n):
			c = mask ^ i    # 按位取反
			if (c>>1)&c==0:
				res.append(f"{i:0{n}b}")
		return res