def length_of_longest_substring(s):
    max_str = 0
    start = 0
    end = 0

    cur_str = set()

    while end < len(s):
        if s[end] not in cur_str:
            cur_str.add(s[end])
            end += 1
            max_str = max(max_str, len(cur_str))
        else:
            cur_str.remove(s[start])
            start += 1
        
    return max_str


print(length_of_longest_substring("abcabcbb"))  # expected 3
print(length_of_longest_substring("bbbbb"))     # expected 1
print(length_of_longest_substring("pwwkew"))    # expected 3
print(length_of_longest_substring("abba"))      # expected 2
print(length_of_longest_substring(""))          # expected 0
print(length_of_longest_substring(" "))         # expected 1
print(length_of_longest_substring("au"))        # expected 2
print(length_of_longest_substring("dvdf"))      # expected 3
print(length_of_longest_substring("tmmzuxt"))   # expected 5
print(length_of_longest_substring("abcdef"))    # expected 6
print(length_of_longest_substring("aab"))       # expected 2
print(length_of_longest_substring("anviaj"))    # expected 5