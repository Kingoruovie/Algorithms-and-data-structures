def add_binary(a, b):
    a_len = len(a)
    b_len = len(b)
    max_of_a_b = max(a_len, b_len)
    i = a_len - 1
    j = b_len - 1
    result = ""

    carry_over = 0
    for _ in range(max_of_a_b): 
        total = 0   
        if i >= 0 and j >= 0:
            total = int(a[i]) + int(b[j]) + carry_over
        elif i >= 0:
            total = int(a[i]) + carry_over
            
        elif j >= 0:
            total = int(b[j]) + carry_over
        remainder = total % 2
        quotient = total // 2
        carry_over = quotient
        result = str(remainder) + result
        i -= 1
        j -= 1
    if carry_over == 1:
        result = str(carry_over) + result
    return result

print(add_binary("11", "11"))