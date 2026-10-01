def valid_anagram(s, t):

    anagram_t = {}
    anagram_s = {}

    for c in s:
        anagram_s[c] = anagram_s.get(c, 0) + 1

    for c in t:
        anagram_t[c] = anagram_t.get(c, 0) + 1

    
    return anagram_t == anagram_s








s = "anagrasm"
t = "nagarams"

print(valid_anagram(s, t))