from collections import deque
from typing import List


class Solution:
	def validStrings(self, n: int) -> List[str]:
		res = ['0', '1']
		dq = deque(res)
		for i in range(1, n):
			for _ in range(len(dq)):
				cur = dq.popleft()
				if cur[-1] == '1':
					dq.append(cur + '0')
				dq.append(cur + '1')
		return list(dq)
