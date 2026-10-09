class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        minwin = float("inf")
        solution = []
        for i in range(len(arr) - k + 1):
            print(i)
            total_dist = 0
            for j in range(i, i + k):
                # sum the absolute distances from each element
                total_dist += abs(arr[j] - x)

            if minwin > total_dist:
                minwin = total_dist
                solution = arr[i:i+k]

        return solution
        