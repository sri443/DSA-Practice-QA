'''You are given a string s and an integer k.

Return the length of the longest substring that contains at most k distinct characters.

Example
Input: s = "eceba", k = 2
Output: 3

Explanation

"ece" → length 3'''

def longestSubstringKDistinct(s, k):
    start = 0
    freq = {}
    max_len = 0

    for end in range(len(s)):
        freq[s[end]] = freq.get(s[end], 0) + 1

        while len(freq) > k:
            freq[s[start]] -= 1
            if freq[s[start]] == 0:
                del freq[s[start]]
            start += 1

        max_len = max(max_len, end - start + 1)

    return max_len
