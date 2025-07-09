class Solution:
    def sumSubMins(self, arr):
        from itertools import chain
        n = len(arr)
        MODULO = 10**9 + 7
        s = [(-1, -1)]
        count = 0
        for end_a in chain(enumerate(arr), [(n, -1)]):
            end, a = end_a
            while s[-1][1] > a:
                mid, val = s.pop()
                start = s[-1][0]
                count += (mid - start) * val * (end - mid)
                count %= MODULO
            s.append(end_a)
        return count
        