def longest_substring(text):

    longest = 0
    start = 0
    end = 0


    sub_s = set()

    for end, c in enumerate(text, start=1):
        while c in sub_s:
            sub_s.remove(text[start])
            start += 1

        sub_s.add(c)
        longest = max(longest, end - start)

    return longest










s = "pwwkew"

print(longest_substring(s))