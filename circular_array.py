def nextGreaterElements(nums: list[int]) -> list[int]: #solution derived from Leetcode, user Marlen09
    stack = []
    result = [-1] *len(nums)


    for _ in range(2):
        for i in range(len(nums)):
            while stack and nums[stack[-1]] < nums[i]:
                result[stack.pop()] = nums[i]

            stack.append(i)

    return result