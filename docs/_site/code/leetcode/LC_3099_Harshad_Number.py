class Solution:
	def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
		
		s = self.sumOfTheDigits(x)
		return -1 if x%s else s

	def sumOfTheDigits(self, x:int):
		res = 0
		while x:
			res+=x%10
			x//=10
		return res