x = list(range(0, 20, 2))

exit()
from LC0724_Find_Pivot_Index_S1_Two_Points import Solution
ans = Solution()
# print(ans.pivotIndex(nums = [1, 7, 3, 6, 5, 6])) # 3
# print(ans.pivotIndex([1,2,3]))  # -1
# print(ans.pivotIndex(nums = [2, 1, -1]))    #  0
print(ans.pivotIndex([-1,-1,-1,-1,-1,0]))



exit()
from LC3200_Maximum_Height_of_a_Triangle_S2_Math import Solution
ans = Solution()
print(ans.maxHeightOfTriangle(red = 2, blue = 4))   # 3
print(ans.maxHeightOfTriangle(red = 2, blue = 1))   # 2
print(ans.maxHeightOfTriangle(red = 1, blue = 1))   # 1
print(ans.maxHeightOfTriangle(red = 10, blue = 1))  # 2
print(ans.maxHeightOfTriangle(red = 9, blue = 3))  # 3


exit()
from LC3200_Maximum_Height_of_a_Triangle_S1_Simulation import Solution
ans = Solution()
print(ans.maxHeightOfTriangle(red = 2, blue = 4))   # 3
print(ans.maxHeightOfTriangle(red = 2, blue = 1))   # 2
print(ans.maxHeightOfTriangle(red = 1, blue = 1))   # 1
print(ans.maxHeightOfTriangle(red = 10, blue = 1))  # 2





exit()
from LC3033_Modify_the_Matrix_S1_Simulation import Solution

ans = Solution()
print(ans.modifiedMatrix(matrix = [[1,2,-1],[4,-1,6],[7,8,9]]))
print(ans.modifiedMatrix(matrix = [[3,-1],[5,2]]))

exit()
from LC3101_Count_Alternating_Subarrays_S1_Sliding_Window import Solution


ans = Solution()
print(ans.countAlternatingSubarrays(nums=[1, 0, 0, 1]))
print(ans.countAlternatingSubarrays(nums=[0, 1, 1, 1]))
print(ans.countAlternatingSubarrays(nums=[0, 1, 0, 1]))
print(ans.countAlternatingSubarrays(nums=[1, 0, 1]))
print(ans.countAlternatingSubarrays(nums=[1]))
print(ans.countAlternatingSubarrays(nums=[1, 1]))
print(ans.countAlternatingSubarrays(nums=[1, 0]))
print(ans.countAlternatingSubarrays([1,0,1,0,1,0,1,0,1,0,0,1,0,1,0,1])) # 76
