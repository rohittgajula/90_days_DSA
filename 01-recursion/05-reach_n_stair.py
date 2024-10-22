# https://www.youtube.com/watch?v=OpzAoNwwYJI&list=PLvg-AaxR3aaZk13DjSEznf848b9lBTeY1&index=3&ab_channel=CuriousChahar

# this is same as fibonacci


class Solution:
    def reach_n_stair(self, n):
        if n == 1:
            return 1
        elif(n == 2):
            return 2
        else:
            return self.reach_n_stair(n-1) + self.reach_n_stair(n-2)



n = 5
solution = Solution()
print(solution.reach_n_stair(n))