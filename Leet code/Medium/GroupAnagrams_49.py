from collections import defaultdict


def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    array_of_answers = []
    first_combinations = defaultdict(list)

    # record letters in dictionary
    for s in strs:
        sorted_s = sorted(s)
        first_combinations[" ".join(sorted_s)].append(s)
    return first_combinations.values()

strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))