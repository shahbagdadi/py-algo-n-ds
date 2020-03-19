nums1 = [1,3,5,9,18,20]
nums2 = [2,4,6,8,10]

a, b = sorted((nums1, nums2), key=len)
print(a)
print(b)