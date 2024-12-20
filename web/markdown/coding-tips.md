---
layout: markdown
---



# Bitwise Operation

1. ```
   1 << n
   2 ** n
   ```

   > 在python中，上述两种方式是等价的，都用来计算2的n次方。

2. ```
   mask = (1 << n) - 1
   ```

   > mask = (1 << n) - 1 主要用于生成一个位掩码，该掩码在低位具有 n 个连续的 1，而高位则为 0

3. 









# 数论

## 异或

1. `Python`和`C++`中的异或符号均为`^`
1. 相同整数（不论正数还是负数）的异或结果为`0`：`x^x=0`
   2. `0`与任何正整数或者负整数异或的结果都等于那个数：`0^3 = 3` 
   3. `偶数`与`偶数+1`的异或结果为`1`（相对应的，`奇数`与`奇数-1`的异或结果为`1`），但是偶数与偶数-1的异或结果不确定（相对应的，奇数与奇数+1的异或结果也不确定）：`odd^(odd-1) = 1`，`even^(even+1) = 1`
   4. 异或满足交换律：`a^b^c = a^c^b = b^a^c = b^c^a = c^a^b = c^b^a`

```python
# Python
print(-1000^-1000)  # 0
print(-312^-311)    # 1
print(45^45)        # 0
print(2^1)          # 3
print(32^31)        # 63
print(32^33)        # 1
```

```c++
// C++
#include <iostream>
using namespace std;
int main()
{
    int a = -1000^-1000;
    int b = -312^-311;
    int c = 45^45;
    int d = 2^1;
    int e = 32^31;
    int f = 32^33;
    cout << "-1000^-1000:" << a <<endl;      // 0
    cout << "-312^-311:" << b <<endl;        // 1
    cout << "45^45:" << c <<endl;            // 0
    cout << "2^1:" << d <<endl;              // 3
    cout << "32^31:" << e <<endl;            // 63
    cout << "32^33:" << f <<endl;            // 1
    system("pause");
    return 0;
}
```

## 与

1. 判断某一个正整数，其二进制表示的倒数第i位是否为1：(num>>i&1)

   ```python
   # 若判断13的二进制表示（1101）的倒数第2位是什么（即是0还是1）：
   print(13>>2&1)		# 1
   # 判断71的二进制表示（1000111）的倒数第i位是什么：
   print(71>>2&1)		# 1
   print(71>>5&1)		# 0
   print(71>>6&1)		# 1
   ```

## 右移 & 左移

一个int类型的num:

- num >> i &1 相当于提取该num的二进制形式中的第i位的数字
- 

## 逻辑运算符

1. Python中，and和or并不返回bool值，而是返回他们实际进行比较的值之一

   ```python
   # and
   print(1 and 0)  # 0
   print(1 and 2)  # 2
   print(1 and 4)  # 4
   print(0 and 1)  # 0
   print(-1 and 8) # 8
   print(-2 and -5)# -5
   # or
   print(1 or 2)   # 1
   print(0 or 2)   # 2
   print(-1 or 2)  # -1
   print(0 or 0)   # 0
   print(0 or -3)  # -3
   ```

2. 但是C++中，&& 和 || 返回bool值，虽然也进行逻辑运算符两边式子的计算，但是整体的逻辑运算符返回bool值

   ```C++
   int a1 = 6;
   bool b = 2 && (a1++);
   cout << boolalpha << a1 << endl;    // 7
   cout << boolalpha << b << endl;     // true
   
   int a2 = 6;
   bool c = 0 && (a2++);
   cout << boolalpha << a2 << endl;    // 6
   cout << boolalpha << c << endl;     // false
   ```

3. 

## 最大公约数（GCD）

最大公约数（Greatest Common Divisor GCD or Highest Common Factor HCF）

欧几里得算法又叫辗转相除法，是指用于计算两个正整数a和b的最大公约数：**以除数和余数反复做除法运算，当余数为0时，取当前算式除数为最大公约数**

其计算原理依赖于下面的定理：**两个整数的最大公约数等于其中较小的那个数和两数相除余数的最大公约数**

```python
def gcd(self, a: int, b: int) -> int:
    """
    用来计算两个正整数a和b的最大公约数
    欧几里得算法（辗转相除法）：
    以除数和余数反复做除法运算，当余数为0时，取当前算式除数为最大公约数
    """
    return a if b==0 else self.gcd(b, a%b)
```

```c++
int gcd(int a, int b){
    /*
    用来计算两个正整数a和b的最大公约数
    欧几里得算法（辗转相除法）：
    以除数和余数反复做除法运算，当余数为0时，取当前算式除数为最大公约数
    */
    return b==0? a: gcd(b, a % b);
}
```

## 最小公倍数（LCM）

最小公倍数（Least Common Multiple）

## GCD和LCM的关系

两个数的乘积等于这两个数的最大公约数和最小公倍数的乘积。假设两个数分别为a和b，他们的最大公约数是gcd，最小公倍数是lcm，则存在这样的关系式：$$a*b=gcd*lcm$$

# 数据结构与算法

## 单调栈

```python
// Python3
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # 解法一：单调栈
        dic = {}
        st = []
        N = len(nums2)
        for i in range(N):
            while st and nums2[i]>st[-1]:
                dic[st.pop()] = nums2[i]
            st.append(nums2[i])
        while st:
            dic[st[-1]] = -1
            st.pop()
        res = []
        for num in nums1:
            res.append(dic[num])
        return res
```

```c++
// C++
#include <iostream>
#include <vector>
#include <stack>
#include <unordered_map>
using namespace std;
class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
        stack<int> st;
        unordered_map<int, int> dic;
        int N=nums2.size();
        for(int i=0; i<N; i++){
            while(!st.empty() && nums2[i]>st.top()){
                dic[st.top()] = nums2[i];
                st.pop();
            }
            st.push(nums2[i]);
        }
        while(!st.empty()){
            dic[st.top()] = -1;
            st.pop();
        }
        vector<int> res;
        for(auto num: nums1){
            res.push_back(dic[num]);
        }
        return res;
    }
};
```



## 二分查找

```python
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        N = len(nums)
        if target<nums[0]:  return 0
        if target>nums[-1]: return N
        l, r = 0, N-1
        while l<=r: 
            mid = (l+r)//2
            if target<nums[mid]:
                r = mid-1
            elif nums[mid]<target:
                l = mid+1
            else:
                return mid
        return l    # 若没查找到target，即返回target的插入位置
```

```c++
class Solution {
public:
    int searchInsert(vector<int>& nums, int target) {
        int N = nums.size();
        if(target<nums[0])      return 0;
        if(target>nums.back())  return N;
        int l=0, r=N-1;
        while(l<=r){
            int mid=(l+r)/2;
            if(nums[mid]<target)
                l = mid+1;
            else if(target<nums[mid])
                r = mid-1;
            else
                return mid;
        }
        return l;   // 若没查找到target，即返回target的插入位置
    }
};
```

## 并查集（union-find disjoint sets）

并查集是一种树型的数据结构，用于处理一些不相交集合的合并及查询问题。并查集的思想是用一个数组表示了整片森林（parent），树的根节点唯一标识了一个集合，我们只要找到了某个元素的树根，就能确定它在哪个集合里。

并查集的主要操作是合并和查询，它是把初始不相交的集合经过多次合并操作后合并为一个大集合，然后通过查询判断两个元素是否在一个大的集合中。

```python
class UnionFind:
    def __init__(self, n):
        '''
        初始化并查集：保证每一个元素都不相交，以等待合并union操作
        '''
        self.parent = list(range(n))
        self.size = [1]*n   # 用作union条件，需要根据题意调整
        self.setCount = n   # 并查集里的集合个数，初始默认相互独立
    def find(self, x):  # 查
        '''
        查找x的根节点
        '''
        if self.parent[x] == x:     # 如果x本身就是根节点，即自己是自己的祖先
            return x
        # 否则继续找x的父亲的祖先
        return self.find(self.parent[x])    # 递归找到x的祖先
    def union(self, x, y):  # 并
        '''
        连通x和y，让y指向x（x<-y）
        '''
        x_root, y_root = self.find(x), self.find(y)
        if x_root == y_root:    # 如果x和y的祖先相同，即在一个集合里
            return
        if self.size[x]< self.size[y]:
            x_root, y_root = y_root, x_root
        self.parent[y_root] = x_root    # 将y的祖先指向x的祖先，即现在y的祖先是x的祖先，实现了并
        self.size[x_root]+=self.size[y_root]
        self.setCount-=1    # 每连通两个节点，集合数减一
    def is_connected(self, x, y):
        '''
        判断x和y连通与否
        '''
        return self.find(x) == self.find(y)
```

## 前缀树

前缀树（Trie数）是一种用于快速检索的多叉数结构，利用字符串的公共前缀来降低复杂度，核心思想是空间换时间，经常用搜索引擎用于文本词频统计

```Python
class Trie:
    def __init__(self):
        self.children = dict()
        self.isEnd = False

    def insert(self, prefix: str) -> None:
        cur = self
        for c in prefix:
            if c not in cur.children:
                cur.children[c] = Trie()
            cur = cur.children[c]
        cur.isEnd = True


    def find_prefix(self, word:str) -> str:
        cur = self
        for i, c in enumerate(word):
            if c not in cur.children:
                return word
            cur = cur.children[c]
            if cur.isEnd:
                return word[:i + 1]
        return word
```



## 前缀和

前缀和的不同写法

```python
# 写法一：新建O(n)空间的写法
def preSum(self, nums):
		N = len(nums)
  	res, pre = [0]*N, 0
  	for i, num in enumerate(nums):
    		pre+=num
    		res[i] = pre
    return res
```

```python
# 写法二：在原数组上修改
def preSum(self, nums):
    for i in range(1, len(nums)):
        nums[i] += nums[i-1]
    return nums
```

## 置换环

环状图：一个有向图如果有n个点，n条边，并且每个点的入度和出度都为1，这样的图被称为环状图。

例如在原数组arr=[2, 0, 1, 4, 3]中，[2, 0, 1]和[4, 3]分别是两个置换环。环与环之间数字不发生交换，只会在环内发生交换。那怎么从原数组中找到一个个环呢？答案是：从第一个数字开始，把这个数字当做下标去访问数组（对于原数组中元素不是某个下标的情况，需要做元素到下标的映射），不断循环知道回到这个数本身。

对于每个环，环内的交换次数为环的大小减一。所以不难推算出：原数组的最小交换次数=原数组大小-环的个数

```python
def swap_cnt(arr):
    N = len(arr)
    s_arr = sorted(arr)
    n2i = {}
    for i in range(N):
        n2i[s_arr[i]] = i   # 每个数字对应的【排序后的位置索引】

    # 看有多少个置换环，环与环之间不会发生交换，只有在环内的两个数字才会发生交换
    loops = 0
    visited = [False]*N
    for i in range(N):
        if visited[i]:
            continue
        while not visited[i]:   # 一步步走完当前的环
            visited[i] = True
            i = n2i[arr[i]]     # 看下当前的数字应该在【排序后的哪个位置】:即把这个数字当做下标去访问数组
        loops += 1    # 环的个数
    return N - loops    # 环内的交换次数为【环的大小-1】，则数组的总交换次数=每个换的环内交换个数之和
```

参考：

1. [BFS + 置换环 + 离散化](https://leetcode.cn/problems/minimum-number-of-operations-to-sort-a-binary-tree-by-level/solution/by-endlesscheng-97i9/)
2. [【算法专题】环状图（置换群）](https://blog.csdn.net/weixin_42638946/article/details/120437662?spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-120437662-blog-46981171.pc_relevant_aa2&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-120437662-blog-46981171.pc_relevant_aa2&utm_relevant_index=1)