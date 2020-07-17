# class Solution:
#     def oddEvenJumps(self, A: List[int]) -> int:
#         count = 0
#         for i in range(len(A)):
#             jump = 1
#             j = i
#             while j < len(A):
#                 if j == len(A) - 1:
#                     count += 1
#                     break
#                 if jump % 2 == 1:
#                     moves = list(filter(lambda x: x >= A[0], A[1:]))
#                     if not len(moves):
#                         break
#                     move = min(moves)
#                 else:
#                     moves = list(filter(lambda x: x <= A[0], A[1:]))
#                     if not len(moves):
#                         break
#                     move = max(moves)
#                 while A[j] != move:
#                     j += 1
#         return count

def oddEvenJumps(A):
    count = 0
    for i in range(len(A)):
        jump = 1
        j = i
        while j < len(A):
            if j == len(A) - 1:
                count += 1
                break
            if jump % 2 == 1:
                moves = list(filter(lambda x: x >= A[j], A[j + 1:]))
                if not len(moves):
                    break
                move = min(moves)
            else:
                moves = list(filter(lambda x: x <= A[j], A[j + 1:]))
                if not len(moves):
                    break
                move = max(moves)
            while A[j + 1] != move:
                j += 1
            jump += 1
            j += 1
    return count

print(oddEvenJumps([10,13,12,14,15]))