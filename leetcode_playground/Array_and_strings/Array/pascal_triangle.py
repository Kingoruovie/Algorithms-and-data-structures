def pascal_triangle(row):
    result = []
    for i in range(0, row):
        inner_list = []
        if i == 0:
            inner_list = [1]
            result.append(inner_list)
        else:
            previous_list = result[i-1]
            left_position = -1
            right_position = 0
            while right_position <= len(previous_list):
                if left_position == -1 or right_position == len(previous_list):
                    inner_list.append(1)
                else:
                    inner_list.append(previous_list[left_position] + previous_list[right_position])
                left_position += 1
                right_position += 1
            result.append(inner_list)
    return result


pasc = pascal_triangle(5)
print(pasc)         
