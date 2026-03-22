class Solution:
    def minAbsDiff(self, grid, k):
        m, n = len(grid), len(grid[0])
        ans = []

        for i in range(m - k + 1):
            row = []
            for j in range(n - k + 1):

                arr = []
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        arr.append(grid[x][y])

                arr = list(set(arr))   # ⭐ FIX
                arr.sort()

                if len(arr) < 2:
                    row.append(0)
                    continue

                min_diff = float('inf')
                for t in range(1, len(arr)):
                    min_diff = min(min_diff, arr[t] - arr[t-1])

                row.append(min_diff)

            ans.append(row)

        return ans