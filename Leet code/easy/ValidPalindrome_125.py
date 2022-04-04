from copy import deepcopy

def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    s = s.lower()
    revised_s = []
    for letter in s:
        if letter.isdigit() or letter.isalpha():
            revised_s.append(letter)
    return revised_s == revised_s[::-1]

    # half = 0
    #
    # for letter in s:
    #     if letter.isdigit() or letter.isalpha():
    #         revised_s.append(letter)
    #
    # if len(revised_s) % 2 == 0:
    #     half = len(revised_s) // 2
    #     other_half = deepcopy(revised_s[half:])
    #     other_half.reverse()
    #     if revised_s[:half] == other_half:
    #         return True
    #     else:
    #         return False
    # else:
    #     half = len(revised_s) // 2 + 1
    #     other_half = deepcopy(revised_s[half:])
    #     other_half.reverse()
    #     if revised_s[:half - 1] == other_half:
    #         return True
    #     else:
    #         return False



print(isPalindrome("aa"))
