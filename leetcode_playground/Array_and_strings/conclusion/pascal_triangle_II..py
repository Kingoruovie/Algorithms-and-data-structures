def getRow(self, rowIndex: int) -> list[int]:
        
        previous_row = None
        ans = [1]
        if rowIndex == 0:
            return ans
        
        for n in range(1, rowIndex + 1):
            i = -1
            j = 0
            previous_row = ans
            ans = []
            while j <= n:
                value = 0
                if i == -1 or j == n:
                    value = 1
                else:
                    value = previous_row[i] + previous_row[j]
                ans.append(value)
                i += 1
                j += 1

        # res = [1]
        # prev = 1
        # for k in range(1, rowIndex + 1):
        #     next_val = prev * (rowIndex - k + 1) // k
        #     res.append(next_val)
        #     prev = next_val
        # return res
        return ans