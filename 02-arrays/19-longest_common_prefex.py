# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".


def longest_common_prefex(strs):
    result = ""

    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return result
        result += strs[0][i]

    return result

def longest_comon_prefex(strs):
    if not strs:
        return ""
    prefex = strs[0]
    for s in strs[1:]:
        i = 0
        while i < len(prefex) and i < len(s) and prefex[i] == s[i]:
            i += 1

        prefex = prefex[:i]

        if not prefex:
            return ""
        
    return prefex

strs = ["flower","flow","flight"]
print(longest_comon_prefex(strs))
print(longest_common_prefex(strs))