def min_sub_array_len(target, nums):
    nums.sort(reverse=True)
    min_sub_array = 0
    current_min_sub_array = 0
    total = 0
    
    for i in range(len(nums)):
        total += nums[i]
        current_min_sub_array += 1
        
        if total >= target:
            if min_sub_array == 0 and current_min_sub_array > 0:
                min_sub_array = current_min_sub_array
            min_sub_array = min(min_sub_array, current_min_sub_array)
            current_min_sub_array = 0
            total = 0
    return min_sub_array


print(min_sub_array_len(213, [12,28,83,4,25,26,25,2,25,25,25,12]))