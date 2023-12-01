def array_pair_sum1(nums):
    nums.sort()
    i = 0
    j = len(nums) - 2
    max_min_sum = 0

    while i <= j:
        if i == j:
            max_min_sum += nums[i]
        else:
            max_min_sum = nums[i] + nums[j]
        i += 2
        j -= 2
    return max_min_sum


def array_pair_sum2(nums):
    return sum(sorted(nums)[::2])


print(array_pair_sum2([15, 14, 13, 12, 11, 10]))