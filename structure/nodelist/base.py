# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#
# class Solution:
#     def getIntersectionNode(self, curA: ListNode, curB: ListNode) -> ListNode:
#         count = 0
#         while curA and curB:
#             curA = curA.next
#             curB = curB.next
#             count += 1
#         if curB:
#             curA = curB
#             while curB:
#                 curB = curB.next
#                 curA = curA.next
#                 count = count - 1
#             curB = curA
#             for i in range(0, count):
#                 curB = curB.next
#                 curA = curA.next
#             if curA == curB:
#                 return curB
#             else:
#                 return None
#         if curA:
#             countB = count

class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        hash = {}
        total = 0
        j = 0
        for i in range(0, len(s)):
            if s[i] in hash.keys():
                total = max(i - j, total)
                j = hash[s[i]] + 1
                hash = {}
                hash.update({s[i]: i})
            else:
                hash.update({s[i]: i})
        total = max(len(hash), total)
        return total


class Solution3:
    def maxArea(self, cost) -> int:
        dp = [0] * (len(cost))
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(2, len(cost)):
            dp[i] = min(dp[i - 1], dp[i - 2]) + cost[i]
        return dp[len(cost)]


class Solution4:
    def merge(self, nums1, m: int, nums2, n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if len(nums2) == 0:
            return None
        res = []
        p1, p2 = 0, 0
        while p1 < m and p2 < n:
            if nums1[p1] < nums2[p2]:
                res.append(nums1[p1])
                p1 += 1
            else:
                res.append(nums2[p2])
                p2 += 1
        if p1 != m:
            res.extend(nums1[p1:])
        if p2 != n:
            res.extend(nums2[p2:])
        nums1 = res
        return None


class Solution5:
    def plusOne(self, digits):
        n = len(digits)
        sing = 0
        for i in range(n - 1, -1, -1):
            if digits[i] != 9:
                digits[i] = digits[i] + 1
                return digits
            else:
                digits[i] = 0
                sing += 1
        if sing != 0:
            res = [1]
            res.extend(digits)
            return res

        return digits


if __name__ == '__main__':
    print(Solution2().lengthOfLongestSubstring(s="abcabcbb"))
    # print(Solution3().maxArea(cost=[1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))
    print(Solution4().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
    # print(Solution5().plusOne([9]))
