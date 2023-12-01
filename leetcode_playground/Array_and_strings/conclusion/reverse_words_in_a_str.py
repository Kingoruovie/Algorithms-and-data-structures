def reverseWords(self, s: str) -> str:
    ls = s.split()
    ls = [string[::-1] for string in ls]
    return ' '.join(ls)