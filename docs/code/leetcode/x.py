from typing import List
from collections import defaultdict

class Solution:
	def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
		n2m = list()
		for ac in accounts:
			name, acs = ac[0], set(ac[1:])
			# print(name, acs)
			if not n2m:
				n2m.append(ac)
				continue
			for i, each in enumerate(n2m):
				k, v = each[0], set(each[1:])
				if acs & v:
					n2m[i] = [k] + list(acs | v)
				else:
					n2m.append(ac)
		print(n2m)
				
			
				


ans = Solution()
print(ans.accountsMerge(
	accounts=[["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"],
	          ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]]
))
"""
[   ["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],
    ["John", "johnnybravo@mail.com"],
	["Mary", "mary@mail.com"]]
"""
