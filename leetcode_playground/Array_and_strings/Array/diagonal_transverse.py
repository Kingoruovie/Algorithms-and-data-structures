def fnname(mat):
    upward_diagonal = True
    downward_diagonal = False
    new_list = []
    m = len(mat) - 1
    n = len(mat[0]) - 1

    i = 0
    j = 0

    new_list.append(mat[i][j])

    while i <= m and j <= n:
        if upward_diagonal:
            if i - 1 >= 0:
                if j + 1 <= n:
                    i -= 1
                    j += 1
                    new_list.append(mat[i][j])
                else:
                    if i + 1 <= m:
                        i += 1
                        new_list.append(mat[i][j])
                        upward_diagonal = False
                        downward_diagonal = True
                    else:
                        break
            else:
                if j + 1 <= n:
                    j += 1
                    new_list.append(mat[i][j])
                    upward_diagonal = False
                    downward_diagonal = True
                else:
                    if i + 1 <= m:
                        i += 1
                        new_list.append(mat[i][j])
                        upward_diagonal = False
                        downward_diagonal = True
                    else:
                        break
        if downward_diagonal:
            if i + 1 <= m:
                if j - 1 >= 0:
                    i += 1
                    j -= 1
                    new_list.append(mat[i][j])
                else:
                    i += 1
                    new_list.append(mat[i][j])
                    upward_diagonal = True
                    downward_diagonal = False
            else:
                if j + 1 <= n:
                    j += 1
                    new_list.append(mat[i][j])
                    upward_diagonal = True
                    downward_diagonal = False
                else:
                    break
    return new_list

            

# def fnname(two_d_list):
#     new_list = []
#     my_dict = {}
#     m = len(two_d_list)
#     n = len(two_d_list[0])
    
#     for i in range(m):
#         for j in range(n):
#             if i + j in my_dict.keys():
#                 my_dict[i+j].append(two_d_list[i][j])
#             else:
#                 my_dict.setdefault(i+j, [two_d_list[i][j]])
#     for key in range(m+n-1):
#         if key % 2 == 0:
#             new_list.extend(my_dict[key][::-1])
#         else:
#             new_list.extend(my_dict[key])
#     return new_list


two_list = [
    [1, 2],
    [3, 4] 
]

print(fnname(two_list))
