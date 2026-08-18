import heapq
from collections import defaultdict

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counts = defaultdict(int)
        for task in tasks:
            counts[task] += 1
        
        heap = []

        for task in counts:
            heapq.heappush(heap, -counts[task])
        
        time = 0
        queue = deque() # tuple of (-count, idle_time)
        while len(heap) or len(queue):
            time += 1
            if len(heap):
                task = heapq.heappop(heap)
                task += 1
                if task != 0:
                    queue.append((task, time + n))

            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])
        
        return time