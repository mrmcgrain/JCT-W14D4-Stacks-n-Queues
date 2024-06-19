def nextGreaterElement(nums1: list[int], nums2: list[int]) -> list[int]: #solution from Leetcode, user yw1033
    mapper = {x:-1 for x in nums1}
    stack = []

    for val in nums2:
        while stack and stack[-1] < val:
            prev_val = stack.pop()
            mapper[prev_val] = val

        stack.append(val)

    return [mapper[x] for x in nums1]