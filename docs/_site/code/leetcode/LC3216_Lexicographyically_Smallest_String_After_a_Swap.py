class Solution:
    def getSmallestString(self, s: str) -> str:
        s_list = list(s)
        for i in range(len(s)-1):
            if (int(s_list[i])+int(s_list[i+1]))%2==0 and int(s_list[i])>int(s_list[i+1]):
                s_list[i], s_list[i+1] = s_list[i+1], s_list[i]
                break
        return ''.join(s_list)