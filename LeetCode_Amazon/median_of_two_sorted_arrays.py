# Merge Sort
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         m = len(nums1)
#         n = len(nums2)
#         is_even = (m + n) % 2 == 0
#         p1 = 0
#         p2 = 0
#         if is_even:
#             med = 0
#             for i in range((m + n) // 2 + 1):
#                 if p1 >= m:
#                     if i == ((m + n) // 2) - 1 or i == (m + n) // 2:
#                         med += nums2[p2]
#                     p2 += 1
#                 elif p2 >= n:
#                     if i == ((m + n) // 2) - 1 or i == (m + n) // 2:
#                         med += nums1[p1]
#                     p1 += 1
#                 else:
#                     if nums1[p1] < nums2[p2]:
#                         if i == ((m + n) // 2) - 1 or i == (m + n) // 2:
#                             med += nums1[p1]
#                         p1 += 1
#                     elif nums1[p1] >= nums2[p2]:
#                         if i == ((m + n) // 2) - 1 or i == (m + n) // 2:
#                             med += nums2[p2]
#                         p2 += 1
#             return med / 2
#         else:
#             for i in range((m + n) // 2 + 1):
#                 if p1 >= m:
#                     if i == ((m + n) // 2):
#                         return nums2[p2]
#                     p2 += 1
#                 elif p2 >= n:
#                     if i == ((m + n) // 2):
#                         return nums1[p1]
#                     p1 += 1
#                 else:
#                     if nums1[p1] < nums2[p2]:
#                         if i == ((m + n) // 2):
#                             return nums1[p1]
#                         p1 += 1
#                     elif nums1[p1] >= nums2[p2]:
#                         if i == ((m + n) // 2):
#                             return nums2[p2]
#                         p2 += 1


# Divide and Conquer
class Solution:
    def kth(self, a, b, k):
        if not a:
            return b[k]
        if not b:
            return a[k]
        a_mid_idx, b_mid_idx = len(a) // 2, len(b) // 2
        a_mid, b_mid = a[a_mid_idx], b[b_mid_idx]
        if a_mid_idx + b_mid_idx < k:
            if a_mid < b_mid:
                return self.kth(a[a_mid_idx + 1 :], b, k - a_mid_idx - 1)
            else:
                return self.kth(a, b[b_mid_idx + 1 :], k - b_mid_idx - 1)
        else:
            if a_mid > b_mid:
                return self.kth(a[:a_mid_idx], b, k)
            else:
                return self.kth(a, b[:b_mid_idx], k)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l = len(nums1) + len(nums2)
        if l % 2 == 1:
            return self.kth(nums1, nums2, l // 2)
        else:
            return (
                self.kth(nums1, nums2, l // 2 - 1) + self.kth(nums1, nums2, l // 2)
            ) / 2
