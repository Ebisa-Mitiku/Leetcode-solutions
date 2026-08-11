class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans=[]

        for i in range(len(nums1)):
            ind=nums2.index(nums1[i])
            if ind!=len(nums2)-1:
                for j in range(ind+1,len(nums2)):
                    if nums2[ind]<nums2[j]:
                        ans.append(nums2[j])
                        break
                else:
                    ans.append(-1)  
            else:
                ans.append(-1)
        return ans
        