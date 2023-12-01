def rotate_array_k_times(nums: list, k: int) -> None:
    # First method: Using the pop and insert method
    # This popping and shifting is done as many times as the times of shift
    # Note that when the shift is more than the list we use modulo because
    # for shift equal to length of nums then nums return to original form.
    # k %= len(nums)
    # for i in range(k):
    #     held_value = nums.pop()
    #     nums.insert(0, held_value)

    # Second method done by creating a new array and doing the shift in that 
    # array and then copying it into nums
    # new_arr = [None] * len(nums)
    # for i in range(len(nums)):
    #     new_arr[(i + k) % len(nums)] = nums[i]

    # for i in range(len(nums)):
    #     nums[i] = new_arr[i]

    # Third method
    # k %= len(nums)
    # new_arr = nums[-k:] + nums[0:k+1]
    # for i in range(len(nums)):
    #     nums[i] = new_arr[i]

    # Fourth method
    nums.reverse()
    k %= len(nums)
    i = 0
    j = len(nums) - 1
    tmp1 = k - 1
    while i < tmp1:
        nums[i], nums[tmp1] = nums[tmp1], nums[i]
        i += 1
        tmp1 -= 1

        
    tmp2 = k
    while tmp2 < j:
        nums[j], nums[tmp2] = nums[tmp2], nums[j]
        tmp2 += 1
        j -= 1
    


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    rotate_array_k_times(nums=nums, k=3)
    print(nums)