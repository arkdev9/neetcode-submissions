from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # slide the window while keeping counts of the
        # letters in the window
        # helper function that checks if the substring counts
        # contain t
        counts, target_counts = defaultdict(int), defaultdict(int)

        for letter in t:
            target_counts[letter] += 1
        
        def does_contain_t():
            for key in target_counts:
                if counts[key] >= target_counts[key]:
                    continue
                return False
            return True

        l, minwin = 0, float("inf")
        start, end = 0, 0
        found = False
        for i in range(len(s)):
            counts[s[i]] += 1

            while does_contain_t():
                # Counts contains target_counts
                # start removing from l
                if i - l < minwin:
                    found = True
                    minwin = i - l
                    start = l
                    end = i
                    
                counts[s[l]] -= 1
                l += 1
            
        return s[start:end + 1] if found else ""


