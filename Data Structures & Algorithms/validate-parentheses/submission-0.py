class Solution:
    def isValid(self, s: str) -> bool:
        stack=deque()
        pair = {
            ']':'[',
            '}':'{',
            ')':'('
        }
        for i in s:
            char="[{("
            if i in char:
                stack.append(i)
            else:
                if not stack:
                    return False
                if stack[-1] == pair[i]:
                    stack.pop()
                else:
                    return False
                    
        return len(stack)==0
            

        