# class Solution:
#     def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
#         points.sort(key = lambda point: point[0]**2 + point[1]**2)
#         return points[:K]

import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        h = []
        for p in points:
            dist = p[0]**2 + p[1]**2
            if len(h) <= K-1:
                heapq.heappush(h,(dist,p))
            else:
                if dist < h[0][0]:
                    heapq.heapreplace(h,(dist,p))
        res = []
        for i in range(K):
            res.append(heapq.heappop(h)[1])
        return res

points = [[3,3],[5,-1],[-2,4]]
K = 2
s = Solution()
print(s.kClosest(points, K))