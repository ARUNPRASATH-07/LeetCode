class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s

        rows = [""] * numRows
        curr_row, step = 0, 1

        for ch in s:
            rows[curr_row] += ch
            if curr_row == 0:
                step = 1
            elif curr_row == numRows - 1:
                step = -1
            curr_row += step

        return "".join(rows)