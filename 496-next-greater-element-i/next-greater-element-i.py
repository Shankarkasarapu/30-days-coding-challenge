class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        
        for i in range(len(nums1)):
            index = nums2.index(nums1[i])
            greater = nums2[index]
            for j in range(index+1, len(nums2)):
                if nums2[j] > greater:
                    greater = nums2[j]
                    break

            if greater == nums2[index]:
                nums1[i] = -1
            else:
                nums1[i] = greater
        return nums1
            
