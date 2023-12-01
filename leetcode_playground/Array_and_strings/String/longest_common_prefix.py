def longest_common_prefix(strs):
    common_prefix = strs[0]

    for index in range(1, len(strs)):
        new_common_prefix = ""
        present_string = strs[index]
        i = 0
        while True:
            if i < len(present_string) and i < len(common_prefix) and common_prefix[i] == present_string[i]:
                new_common_prefix += common_prefix[i]
                i += 1
            else:
                break
        common_prefix = new_common_prefix
    return common_prefix

trial_list1 = ["flower","flow","flight"]
trial_list2 = ["dog","racecar","car"]
print(type(longest_common_prefix(trial_list2)))