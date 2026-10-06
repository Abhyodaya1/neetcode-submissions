class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        
        while left < right:
            # Skip non-alphanumeric characters from left
            if not s[left].isalnum():
                left += 1
                continue
                
            # Skip non-alphanumeric characters from right
            if not s[right].isalnum():
                right -= 1
                continue
            
            # Compare lowercase versions of both characters
            if s[left].lower() != s[right].lower():
                return False
                
            # Move both pointers inward when characters match
            left += 1
            right -= 1
            
        return True