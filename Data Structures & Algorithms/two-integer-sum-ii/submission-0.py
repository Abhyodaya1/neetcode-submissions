
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        n1, n2 = 0, len(numbers) - 1

        while n1 < n2:

            current_sum = numbers[n1] + numbers[n2]

            if current_sum > target:
                n2 -= 1

            elif current_sum < target:
                n1 += 1

            else:
                return [n1 + 1, n2 + 1]
