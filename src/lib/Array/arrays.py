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


def topKFrequentN2(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    frequency = defaultdict(int)

    for n in nums:
        frequency[n] += 1
        
    opt = []
    while k > 0:
        max_key = float('-inf')
        max_val = 0
        for key, val in frequency.items():
            if val > max_val:
                max_key = key
                max_val = val
            
        opt.append(max_key)
        del frequency[max_key]
        k -= 1
        
    return opt

def topKFrequentN(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)
        
    for n, c in count.items():
        freq[c].append(n)

    res = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
    
if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    nums = topKFrequentN(nums, 2)
    print(nums)