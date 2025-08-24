class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        for i in nums2:
            nums1.append(i)
        nums1.sort()
        n=len(nums1)
        if n%2!=0:
            return nums1[n//2]
        elif n%2==0:
            
            return float(nums1[(n//2)-1]+nums1[(n//2)])/2
