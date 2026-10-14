class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        products = [1] * (length)

        # calculate prefix products
        prefix = [1] * (length)
        prefix[0] = nums[0]
        for i in range(1, length):
            prefix[i] = prefix[i-1] * nums[i]
        
        # calculate suffix products
        suffix = [1] * (length)
        suffix[length-1] = nums[length-1]
        for i in range(length - 2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i]

        # splice prefix and suffix
        for j in range(0, length):
            if (j - 1 >= 0): #has prefix
                products[j] = products[j] * prefix[j-1]
            if (j + 1 < length): #has suffix
                products[j] = products[j] * suffix[j+1]

        return products