def reverseWords(self, s: str) -> str:
    # Note that the split when not given any argument will split with
    # an arbitrary number of of spaces i.e ' ' or '  ' or even '    '
    ls = s.split()
    return ' '.join(ls[::-1])
        

