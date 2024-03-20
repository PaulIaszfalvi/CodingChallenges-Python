class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # Solution (Online)

        task_counts = Counter(tasks)
        max_heap = [(-count, task) for task, count in task_counts.items()]
        heapq.heapify(max_heap)
        cycle = 0
        
        while max_heap:
            temp = []
            for _ in range(n + 1):
                if max_heap:
                    count, task = heapq.heappop(max_heap)
                    count += 1
                    if count < 0:
                        temp.append((count, task))
                cycle += 1
                if not max_heap and not temp:
                    break
            for item in temp:
                heapq.heappush(max_heap, item)
        
        return cycle

        # Rough Solution 1
        
        if n == 1:
            return len(tasks)

        d = {}
        l = ['' for _ in range(len(tasks) * n)]
        i = 0

        for x in tasks:
            d[x] = d.get(x, 0) + 1

        for k, v in d.items():
            c = 0            
            while v > 0:
                l.insert(i + (n+1) * c, k)
                v -= 1
                c += 1
            i += 1
        print(l)