def needle_in_haystack(haystack, needle):
    result = []

    i = 0
    while i < len(haystack):
        if haystack[i] == needle[0]:
            if haystack[i:i+len(needle)] == needle:
                result.append(i)
                i += len(needle)
            else:
                i += 1
        else:
            i += 1

    
    if result:
        return 0, result
    return -1


print(needle_in_haystack("sdbobsadbob", "sad"))