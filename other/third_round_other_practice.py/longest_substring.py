
def length_of_longest_substring(word):
    max_length = 0
    start = 0
    end = 0

    substring = set()

    while end < len(word):
        if word[end] not in substring:
            substring.add(word[end])
            end += 1
            max_length = max(max_length, len(substring))
        else:
            substring.remove(word[start])
            start += 1
    return max_length









print(length_of_longest_substring("abcabcbb"))  # expected: 3
print(length_of_longest_substring("bbbbb"))     # expected: 1
print(length_of_longest_substring("pwwkew"))    # expected: 3
print(length_of_longest_substring(""))          # expected: 0
print(length_of_longest_substring("dvdf"))      # expected: 3