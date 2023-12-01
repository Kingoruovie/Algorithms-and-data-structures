def remove_duplicate(nums: list) -> int:
    i = 0
    j = 1
    current_number = nums[0]
    while j < len(nums):
        if nums[j] == current_number:
            nums[j] = '_'
        else:
            i += 1
            current_number = nums[j]
            nums[i], nums[j] = nums[j], nums[i]
        j += 1

    return i + 1



if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3, 4]
    k = remove_duplicate(nums)
    print(nums)
    print(k)