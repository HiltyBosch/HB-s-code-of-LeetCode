class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if nums1.__len__() == 0:
            if nums2.__len__() == 0:
                return 0.0
            else:
                if nums2.__len__()%2 ==1:
                    return float(nums2[(nums2.__len__()-1)/2])
                else:
                    return float(nums2[(nums2.__len__()-1)/2] +nums2[nums2.__len__()/2])/2
        oddFlag = (nums1.__len__() + nums2.__len__())%2 == 1 #odd ji even ou
        if nums2.__len__() == 0:
            return self.findMedianSortedArrays(nums2,nums1)
        halfNum = (nums1.__len__()+ nums2.__len__() +1)/2 #num of half of the nums,range(1,+)
        # all of num1 <or > num2's middle , the two index in one list
        def getadge(nums1,nums2,oddFlag):
            edgeFlag = True
            if nums1.__len__() <= nums2.__len__():
                #[num2num2num2num2,[num1],num2]
                if oddFlag:
                    if nums1[0] > nums2[halfNum-1]:
                        return float(nums2[halfNum-1]),edgeFlag
                    if nums1[-1] < nums2[halfNum - nums1.__len__()-1]:
                        return  float(nums2[halfNum-nums1.__len__()-1]),True
                else:
                    if nums2.__len__() == 1:
                        return float(nums1[0]+nums2[0])/2,edgeFlag
                    if nums2.__len__() == nums1.__len__():
                        if nums1[0] >= nums2[-1]:
                            return float(nums1[0] + nums2[-1])/2,True
                        if nums1[-1] <=nums2[0]:
                            return float(nums1[-1] + nums2[0])/2,True
                        return 0.0,False
                    if nums1[0] >nums2[halfNum-1]:
                        small = nums1[0] if nums1[0] < nums2[halfNum] else nums2[halfNum]
                        return float(nums2[halfNum-1] + small)/2,edgeFlag
                    if nums1[-1] < nums2[halfNum - nums1.__len__()]:
                        large = nums1[-1] if nums1[-1] > nums2[halfNum - nums1.__len__()-1] else nums2[halfNum - nums1.__len__()-1]
                        return float(large + nums2[halfNum - nums1.__len__()])/2 , True
            edgeFlag = False
            return 0.0,edgeFlag
        edgereturn = getadge(nums1,nums2,oddFlag)
        if edgereturn[1]:
            return edgereturn[0]
        edgereturn = getadge(nums2,nums1,oddFlag)
        if edgereturn[1]:
            return edgereturn[0]

        mid1 = (nums1.__len__()-1)/2                      #index of the num1's middle
        mid2 = (nums2.__len__()-1)/2                      #index of the num2's middle
        if nums1.__len__()%2 ==1 and nums2.__len__()%2 == 1:
            if nums1.__len__() == 1:
                mid2 -= 1
            elif nums2.__len__() == 1:
                mid1 -= 1
            else:
                mid1 -=1
        midPre = halfNum - nums2.__len__()-1 if nums2.__len__() <halfNum else 0
        midBack = halfNum-1 if nums1.__len__() >halfNum else nums1.__len__()
        if mid1 == 0 and mid2 != 0 and nums1.__len__() != 1:
            if nums1[mid1] > nums2[mid2+1] or nums1[mid1+1]< nums2[mid2]:
                mid1 =1
                mid2 -=1
        elif mid2 == 0 and mid1 != 0 and nums2.__len__() != 1:
            if nums1[mid1] > nums2[mid2+1] or nums1[mid1+1]< nums2[mid2]:
                mid2 =1
                mid1 -=1
        while 1:
            if mid2 != nums2.__len__()-1 and nums1[mid1] > nums2[mid2+1]:
                midBack = mid1
                mid1 = midPre +(mid1 - midPre)/2
                mid2 = halfNum - mid1 -2
                continue
            if mid1 !=nums1.__len__()-1 and nums1[mid1+1] < nums2[mid2]:
                midPre = mid1 +1
                mid1 += (midBack - mid1)/2
                mid2 = halfNum - mid1 -2
                continue
            break
        if oddFlag:
            return float(nums1[mid1]) if nums1[mid1] > nums2[mid2] else float(nums2[mid2])
        else:
            if mid1 == nums1.__len__()-1:
                small = nums1[mid1] if nums1[mid1] > nums2[mid2] else nums2[mid2]
                return float(small + nums2[mid2+1])/2
            elif mid2 == nums2.__len__()-1:
                small = nums2[mid2] if nums2[mid2] > nums1[mid1] else nums1[mid1]
                return float(small + nums1[mid1+1])/2
            else:
                small = nums1[mid1] if nums1[mid1] > nums2[mid2] else nums2[mid2]
                big = nums1[mid1+1] if nums1[mid1+1] < nums2[mid2+1] else nums2[mid2+1]
                return float(small + big)/2



    def right(self,nums1,nums2):
        lenOfAll = nums1.__len__() + nums2.__len__()
        midddleCount = (lenOfAll + 1) / 2
        ind1, ind2 = 0, 0
        resultMid = 0
        if nums2.__len__() ==0 :
            if nums1.__len__()%2 == 1:
                return nums1[nums1.__len__()/2]
            else:
                return float(nums1[nums1.__len__()/2] + nums1[nums1.__len__()/2 - 1])/2
        elif nums1.__len__() == 0:
            if nums2.__len__()%2 == 1:
                return nums2[nums2.__len__()/2]
            else:
                return float(nums2[nums2.__len__()/2] + nums2[nums2.__len__()/2 - 1])/2
        if lenOfAll%2 == 1:
            while midddleCount != 0:
                if ind2 == nums2.__len__() or (ind1 != nums1.__len__() and nums1[ind1] < nums2[ind2]):
                    resultMid = nums1[ind1]
                    ind1 +=1
                else:
                    resultMid = nums2[ind2]
                    ind2 += 1
                midddleCount -= 1
        else:
            resultMid1 ,resultMid2 = 0,0
            while midddleCount != -1:
                if  ind2 == nums2.__len__() or (ind1 != nums1.__len__() and nums1[ind1] < nums2[ind2]):
                    resultMid1 = resultMid2
                    resultMid2 = nums1[ind1]
                    ind1 += 1
                else:
                    resultMid1 = resultMid2
                    resultMid2 = nums2[ind2]
                    ind2 += 1
                midddleCount -= 1
            resultMid = float(resultMid1 + resultMid2)/2.0
        return resultMid




if __name__ == '__main__':
    solution = Solution()
    print solution.findMedianSortedArrays([1,3,5,7,9,11,13,17],[2,4,6,8,10])
    print solution.right([1,3,5,7,9,11,13,17],[2,4,6,8,10])
    print solution.findMedianSortedArrays([1,2,3,4],[5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21])
    print solution.right([1,2,3,4],[5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21])
    print solution.findMedianSortedArrays([19,20,21],[1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18])
    print solution.right([19,20,21],[1,2,3,5,6,7,8,9,10,11,12,13,14,15,16,17,18])
    print solution.findMedianSortedArrays([1],[2])
    print solution.right([1],[2])
    print solution.findMedianSortedArrays([2],[-1])
    print solution.right([2],[-1])
    print solution.findMedianSortedArrays([1,2,3,4,5],[1,2,3,4,5])
    print solution.right([1,2,3,4,5],[1,2,3,4,5])
    print solution.findMedianSortedArrays([1,32,45,67,134],[1,23,37,263,734])
    print solution.right([1,32,45,67,134],[1,23,37,263,734])
    print solution.findMedianSortedArrays([1,2,3,4,5,6],[7,8,9])
    print solution.right([1,2,3,4,5,6],[7,8,9])
    print solution.findMedianSortedArrays([2,3,4,5],[1])
    print solution.right([2,3,4,5],[1])
    print solution.findMedianSortedArrays([1,3,4,5],[2])
    print solution.right([1,3,4,5],[2])
    print solution.findMedianSortedArrays([2,4,5,6,7],[1,3])
    print solution.right([2,4,5,6,7],[1,3])
    print solution.findMedianSortedArrays([1,2,3,4,6],[5])
    print solution.right([1,2,3,4,6],[5])
    print solution.findMedianSortedArrays([1,2,4],[3,5,6,7])
    print solution.right([1,2,4],[3,5,6,7])
    print solution.findMedianSortedArrays([1,3],[2])
    print solution.right([1,3],[2])
    print solution.findMedianSortedArrays([2],[1,3,4])
    print solution.right([2],[1,3,4])
    print solution.findMedianSortedArrays([2,4,5],[1,3])
    print solution.right([2,4,5],[1,3])
    print solution.findMedianSortedArrays([4,6],[1,2,3,5])
    print solution.right([4,6],[1,2,3,5])
    print solution.findMedianSortedArrays([1,6],[5,7,9,10])
    print solution.right([1,6],[5,7,9,10])
    print solution.findMedianSortedArrays([1,2,5],[3,4,6])
    print solution.right([1,2,5],[3,4,6])
    print solution.findMedianSortedArrays([2,3,4,7],[1,5,6])
    print solution.right([2,3,4,7],[1,5,6])
    print solution.findMedianSortedArrays([1,2,3,7,8],[4,5,6,9,10])
    print solution.right([1,2,3,7,8],[4,5,6,9,10])
    print solution.findMedianSortedArrays([3] , [1,2,4,5])
    print solution.right([3] , [1,2,4,5])
    print solution.findMedianSortedArrays([1,3],[2,4,5])
    print solution.right([1,3],[2,4,5])
    print solution.findMedianSortedArrays([1],[2])
    print solution.right([1],[2])
    print solution.findMedianSortedArrays([1,2],[3])
    print solution.right([1,2],[3])
    print solution.findMedianSortedArrays([1],[3,4])
    print solution.right([1],[3,4])
    print solution.findMedianSortedArrays([5],[3,4])
    print solution.right([5],[3,4])
    print solution.findMedianSortedArrays([1,2],[3,4])
    print solution.right([1,2],[3,4])
    print solution.findMedianSortedArrays([5,6],[3,4])
    print solution.right([5,6],[3,4])
    print solution.findMedianSortedArrays([1,2,3],[4,5,6])
    print solution.right([1,2,3],[4,5,6])
    print solution.findMedianSortedArrays([7,8,9],[4,5,6])
    print solution.right([7,8,9],[4,5,6])
    print solution.findMedianSortedArrays([1,2,4,5],[3])
    print solution.right([1,2,4,5],[3])
