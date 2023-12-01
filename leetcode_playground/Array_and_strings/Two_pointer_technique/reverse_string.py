def reverse_string(s: list) -> None:
    i = 0
    j = len(s) - 1
    while i < j:
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1


s_1 = ["o", "v", "i", "e"]
s_2 = ["h", "e", "l", "l", "o"]

reverse_string(s_1)
reverse_string(s_2)

print(s_1)
print(s_2)