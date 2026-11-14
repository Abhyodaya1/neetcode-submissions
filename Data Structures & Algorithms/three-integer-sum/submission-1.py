
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        answer = []

        for i in range(len(nums)):

            # Skip duplicate first elements
            if i > 0 and nums[i] == nums[i-1]:
                continue

            j = i + 1
            k = len(nums) - 1

            while j < k:

                current_sum = nums[i] + nums[j] + nums[k]

                if current_sum > 0:
                    k -= 1

                elif current_sum < 0:
                    j += 1

                else:
                    answer.append([nums[i], nums[j], nums[k]])

                    j += 1
                    k -= 1

                    # Skip duplicate second elements
                    while j < k and nums[j] == nums[j-1]:
                        j += 1

        return answer
