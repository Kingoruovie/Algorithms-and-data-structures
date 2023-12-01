def find_max_consecutive_ones(nums):
    count = 0
    current_max = 0
    for i in range(len(nums)):
        if nums[i] == 1:
            count += 1
            if count > current_max:
                current_max = count
        else:
            count = 0
    return current_max

print(find_max_consecutive_ones([1,1,0,1,1,1]))