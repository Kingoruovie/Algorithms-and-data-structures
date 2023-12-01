def move_zero(nums: list) -> None:
    i = 0
    for j in range(len(nums)):
        if nums[j] == 0:
            continue
        else:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1

        

if __name__ == "__main__":
    nums = [1,2, 0, 0, 9, 6]
    move_zero(nums)
    print(nums)