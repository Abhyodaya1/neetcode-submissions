class Solution:

    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        freq = [[] for i in range(n + 1)]

        # 1. Initialize and fill the count dictionary
        count = {}
        for num in nums:  # Changed 'n' to 'num' to avoid overwriting the length 'n'
            count[num] = count.get(num, 0) + 1

        # 2. Map frequencies into the bucket list
        # Changed loop variables to 'num, f' to avoid conflicting with the function argument 'k'
        for num, f in count.items():
            freq[f].append(num)  # Changed 'c' to the actual frequency 'f'

        # 3. Gather the top K elements by iterating backward
        res = []
        for i in range(len(freq) - 1, 0, -1):  # Added missing colon
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
