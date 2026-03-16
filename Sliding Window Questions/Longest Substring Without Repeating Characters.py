'''Given a string s, return the length of the longest substring that contains no repeating characters.

A substring must be contiguous. '''

def lengthOfLongestSubstring(s):
  
    start=0
    freq=set()
    max_length=0
  
    for end in range(len(s)):
      
        while s[end] in freq:
          
            freq.remove(s[start])
            start+=1
          
        freq.add(s[end])
      
        max_length=max(max_length, end-start+1)
      
    return max_length
