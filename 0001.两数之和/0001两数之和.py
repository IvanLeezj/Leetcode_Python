class Solution():
    def twoSum(self, nums, target):
        """
        两数之和返回
        :param nums: list[int]
        :param target: int
        :return: list[int]
        """
        dic = {}
        for i, num in enumerate(nums):
            if target - num in dic:
                return [dic[target - num], i]
            dic[num] = i

if __name__ == '__main__':
    test = Solution()
    print(test.twoSum([1, 2, 3, 5], 6))