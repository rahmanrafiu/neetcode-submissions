class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        largest = 0

        for n in nums:
            if (n - 1) not in numSet:
                length = 0
                while (n + length) in numSet:
                    length += 1
                if length > largest:
                    largest = length
        
        return largest

                