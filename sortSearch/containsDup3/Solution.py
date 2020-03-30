from typing import List

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        # Bucket sort. Each bucket has size of t. For each number, the possible
        # candidate can only be in the same bucket or the two buckets besides.
        # Keep as many as k buckets to ensure that the difference is at most k.
        if t < 0:
            return False
        buckets = {}
        for i in range(len(nums)):
            if i-k > 0:
                bucket_id_to_delete = nums[i-k-1]//(t+1)
                del buckets[bucket_id_to_delete]
            bucket_id = nums[i]//(t+1)
            condition1 = (bucket_id in buckets)
            condition2 = ((bucket_id-1 in buckets and abs(buckets[bucket_id-1]-nums[i])<= t))
            condition3 = ((bucket_id+1 in buckets and abs(buckets[bucket_id+1]-nums[i])<= t))
            if condition1 or condition2 or condition3:
                return True
            buckets[bucket_id] = nums[i]
        return False

s = Solution()
print(s.containsNearbyAlmostDuplicate([1,5,9,1,5,9],2,3))