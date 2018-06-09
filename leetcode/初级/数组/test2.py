class Solution:
    def rotate(self, nums):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 1
        
        while(i < j):
            for j in range(i+1, len(nums)-1):
                if nums[j] != nums[i]:
                    break
            else:
                del nums[i+1:j]
            i += 1
            
        return len(nums)

def main():
    a = [1,1,2]
    Solution().rotate(a)
    print(a)

if __name__ == '__main__':
    main()