class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        count = {}

        for ta in tasks:
            count[ta] = count.get(ta, 0) + 1

        max_freq = max(count.values())

        count_max = list(count.values()).count(max_freq)

        return max(len(tasks), (max_freq-1) * (n+1) + count_max)
