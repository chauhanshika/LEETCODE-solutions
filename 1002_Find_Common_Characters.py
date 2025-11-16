class Solution(object):
    def commonChars(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        
        min_freq = [float("inf")] * 26
        
        for word in words:
            freq = [0] * 26
            for c in word:
                freq[ord(c) - ord('a')] += 1
            # Step 2: take min frequency across all words
            for i in range(26):
                min_freq[i] = min(min_freq[i], freq[i])
        
        
        res = []
        for i in range(26):
            res.extend([chr(i + ord('a'))] * min_freq[i])
        
        return res
