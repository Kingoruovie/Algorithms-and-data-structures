def remove_element(nums, val):
    left = 0
    right = len(nums) - 1
    while left <= right:
        if nums[left] != val:
            left += 1
        else:
            nums[left] = nums[right]
            nums[right] = "_"
            right -= 1
    return left, nums


ls = [3, 3, 3, 5,3, 3]
print(remove_element(ls, 3))