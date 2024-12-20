from typing import List


class Solution:
	def validStrings(self, n: int) -> List[str]:
		if n == 1:
			return ['0', '1']
		res = []
		for each in self.validStrings(n - 1):
			if each[-1] != '0':
				res.append(each + '0')
			res.append(each + '1')
		return res
