class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Step 1: Count frequency of each number
        count = Counter(nums)
        
        # Step 2: Sort the unique keys based on their frequency count (descending)
        # key=lambda x: count[x] sorts by the frequency value
        sorted_elements = sorted(count.keys(), key=lambda x: count[x], reverse=True)
        
        # Step 3: Take the first k elements
        return sorted_elements[:k]
        