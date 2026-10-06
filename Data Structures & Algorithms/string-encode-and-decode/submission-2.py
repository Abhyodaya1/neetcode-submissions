class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes,res = [],[]
        for s in strs:
            sizes.append(str(len(s)))
            sizes.append(',')
        sizes.append('#')
        sizes.extend(strs)
        return ''.join(sizes)
        
    def decode(self, s: str) -> List[str]:
        if not s:
            return []

        sizes, res, i = [], [], 0

        # Read the header until we hit the '#' marker
        while s[i] != "#":
            if s[i] == ",":
                i += 1
                continue

            # Scan ahead to grab the complete multi-digit number
            j = i
            while s[j] != "," and s[j] != "#":
                j += 1

            sizes.append(int(s[i:j]))  # Correctly parses '11' instead of '1'
            i = j  # Move pointer past the parsed number

        i += 1  # Step completely over the '#' marker

        # Extract the original strings based on the recorded sizes
        for sz in sizes:
            res.append(s[i : i + sz])
            i += sz

        return res