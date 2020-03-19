from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2) < len(nums1) :   # logic below expects num1 to be shorter of the two
            nums1,nums2 = nums2,nums1
        L1 , L2 = len(nums1) , len(nums2)
        is_even = (L1 + L2) % 2 == 0
        l1 , r1 = 0, L1
        while l1 <= r1 :
            p1 = (l1 + r1) // 2 # start with mid in the first list as p1
            p2 = (L1 + L2) // 2 - p1 # 2*(p1 + p2 ) == L1 + L2 
            # print(f'p1= {p1} p2 = {p2}')
            if p1 < L1 and (nums2[p2 -1] > nums1[p1]):
                l1 = p1 + 1
            elif p1 > 0 and (nums1[p1-1] > nums2[p2]) :
                r1 = p1 - 1
            else :
                if p1 == L1:
                    rmax = nums2[p2]
                elif p2 == L2 :
                    rmax = nums1[p1]
                else:
                    rmax = min(nums1[p1],nums2[p2])

                if is_even : 
                    if p1 == 0:
                        lmax = nums2[p2 - 1]
                    elif p2 == 0 :
                        lmax = nums1[p1 -1]
                    else:
                        lmax = max(nums1[p1-1], nums2[p2-1])
                    return (rmax + lmax) / 2
                else :                
                    return rmax


s = Solution()
n2 = [2]
n1 = []
print(s.findMedianSortedArrays(n1,n2))


