'''Given a string s and integer k, you may replace at most k characters.

Return the length of the longest substring that can become all the same character 

after at most k replacements.'''

def characterReplacement(s, k):
    start = 0
    freq = {}
    max_freq = 0
    max_len = 0

    for end in range(len(s)):
        freq[s[end]] = freq.get(s[end], 0) + 1
        max_freq = max(max_freq, freq[s[end]])

        while (end - start + 1) - max_freq > k:
            freq[s[start]] -= 1
            start += 1

        max_len = max(max_len, end - start + 1)

    return max_len
