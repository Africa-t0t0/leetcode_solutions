import numpy as np

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        aux = nums1 + nums2
        aux.sort()
        vector = np.array(aux)
        media = np.median(vector)
        return media

