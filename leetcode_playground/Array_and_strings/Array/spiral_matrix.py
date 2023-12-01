# def spiral_matrix(matrix):
#     m = len(matrix)
#     n = len(matrix[0])
#     i = 0
#     j = 0
#     element_count = m * n
#     dict_of_position = {'0,0': '0,0'}
#     new_list = [matrix[0][0]]
#     direction = "right"

#     while len(dict_of_position) < element_count:
#         if direction == "right":
#             if j+1 < n and (f'{i},{j+1}' not in dict_of_position):
#                     j += 1
#                     new_list.append(matrix[i][j])
#                     dict_of_position[f'{i},{j}'] = f'{i},{j}'
#             else:
#                 if i+1 < m and (f'{i+1},{j}' not in dict_of_position):
#                     i += 1
#                     direction = "down"
#                     new_list.append(matrix[i][j])
#                     dict_of_position[f'{i},{j}'] = f'{i},{j}'
            
            
#         elif direction == "down":
#             if i+1<m and (f'{i+1},{j}' not in dict_of_position):
#                 i += 1
#                 new_list.append(matrix[i][j])
#                 dict_of_position[f'{i},{j}'] = f'{i},{j}'
#             else:
#                 if j - 1 >= 0 and (f'{i},{j-1}' not in dict_of_position):
#                     j -= 1
#                     direction = "left"
#                     new_list.append(matrix[i][j])
#                     dict_of_position[f'{i},{j}'] = f'{i},{j}'
            
#         elif direction == "left":
#             if j - 1 >= 0 and (f'{i},{j-1}' not in dict_of_position):
#                 j -= 1
#                 new_list.append(matrix[i][j])
#                 dict_of_position[f'{i},{j}'] = f'{i},{j}'
#             else:
#                 if i - 1 >= 0 and (f'{i-1},{j}' not in dict_of_position):
#                     i -= 1
#                     direction = "up"
#                     new_list.append(matrix[i][j])
#                     dict_of_position[f'{i},{j}'] = f'{i},{j}'

            
#         elif direction == "up":
#             if i - 1 >= 0 and (f'{i-1},{j}' not in dict_of_position):
#                 i -= 1
#                 new_list.append(matrix[i][j])
#                 dict_of_position[f'{i},{j}'] = f'{i},{j}'
#             else:
#                 if j + 1 < n and (f'{i},{j+1}' not in dict_of_position):
#                     j += 1
#                     new_list.append(matrix[i][j])
#                     dict_of_position[f'{i},{j}'] = f'{i},{j}'
#                     direction = "right"

#     return new_list


def spiral_matrix(matrix):
    new_list = []
    m = len(matrix)
    n = len(matrix[0])
    i = 0
    j = 0
    element_count = m * n
    spiral_count = 0
    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    current_direction = 0

    def in_range(row, col):
        if row >= 0 and row < m and col >= 0 and col < n:
            return True
        return False
    
    while spiral_count < element_count:
        new_list.append(matrix[i][j])
        spiral_count += 1
        matrix[i][j] = None

        next_row = i + direction[current_direction][0]
        next_col = j + direction[current_direction][1]

        if not in_range(next_row, next_col) or matrix[next_row][next_col] == None:
            current_direction = (current_direction + 1) % 4
            next_row = i + direction[current_direction][0]
            next_col = j + direction[current_direction][1]
        i = next_row
        j = next_col

    return new_list
            



two_d_list = [
    [1, 2, 3, "a"],
    [4, 5, 6, "b"],
    [7, 8, 9, "c"],
    # [10, 11, 12, 'd']
]

print(spiral_matrix(two_d_list))