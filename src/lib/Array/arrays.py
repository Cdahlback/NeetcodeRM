from collections import defaultdict


def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """

    res = defaultdict(list)
    for s in strs:
        count = [0] * 26 # a .. z

        for c in s:
            count[ord(c) - ord("a")] += 1
            
        res[tuple(count)].append(s)

    return list(res.values())


if __name__ == "__main__":
    strs = ["eat", "ate", "tan", "nat", "can"]
    result = groupAnagrams(strs)
    print(result)