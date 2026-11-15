
class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # 1. Build the required frequency map
        need = {}

        for char in t:
            need[char] = need.get(char, 0) + 1

        # 2. Initialize sliding window
        window = {}
        required = len(need)
        formed = 0

        left = 0
        min_len = float('inf')
        start = 0

        # 3. Expand the window using right pointer
        for right in range(len(s)):

            char = s[right]
            window[char] = window.get(char, 0) + 1

            # Check if this character satisfies its requirement
            if char in need and window[char] == need[char]:
                formed += 1

            # 4. Shrink the window while it remains valid
            while formed == required:

                # Calculate current window length
                current_len = right - left + 1

                # Store the smallest valid window
                if current_len < min_len:
                    min_len = current_len
                    start = left

                # Remove the leftmost character
                left_char = s[left]

                if left_char in need and window[left_char] == need[left_char]:
                    formed -= 1

                window[left_char] -= 1
                left += 1

        # 5. Return the answer
        if min_len == float('inf'):
            return ""

        return s[start:start + min_len]
