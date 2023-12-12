from collections import defaultdict
import collections


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


def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    rows = collections.defaultdict(set)
    cols = collections.defaultdict(set)
    squares = collections.defaultdict(set) # Key = (r // 3, c // 3)

    for r in range(9):
        for c in range(9):
            if board[r][c] == ".":
                continue
            if (board[r][c] in rows[r] or
                board[r][c] in cols[c] or
                board[r][c] in squares[(r//3, c//3)]):
                return False
            else:
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])
    return True
    
if __name__ == "__main__":
    board = [
     ["5","3",".","7","7",".",".",".","."]
    ,["6",".",".","1","9","5",".",".","."]
    ,[".","9","8",".",".",".",".","6","."]
    ,["8",".",".",".","6",".",".",".","3"]
    ,["4",".",".","8",".","3",".",".","1"]
    ,["7",".",".",".","2",".",".",".","6"]
    ,[".","6",".",".",".",".","2","8","."]
    ,[".",".",".","4","1","9",".",".","5"]
    ,[".",".",".",".","8",".",".","7","9"]
    ]
    boolean = isValidSudoku(board)
    print(boolean)