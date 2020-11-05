# 给定一个整数数组nums和一个目标值target，请你在该数组中找出和为目标值的那
# 两个整数，并返回他们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素不能使用两遍。
#
# 示例:
# 给定
# nums = [2, 7, 11, 15], target = 9
# 因为
# nums[0] + nums[1] = 2 + 7 = 9
# 所以返回[0, 1]

# 方法一
def twoSum1(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    length = len(nums)
    for x in range(0, length):
        for y in range(x + 1, length):
            if nums[x] + nums[y] == target:
                return x, y

# 方法二
def twoSum2(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    length = len(nums)
    for i in range(0, length):
        if target - nums[i] in nums[i + 1:]:
            j = nums[i + 1:].index(target - nums[i]) + i + 1
            return (i, j)


nums = [2, 7, 11, 15]
target = 9
print(twoSum2(nums, target))
