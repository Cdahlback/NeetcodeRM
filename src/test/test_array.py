
from pathlib import Path
import sys
print(str(Path(__file__).parent.parent))
sys.path.append(str(Path(__file__).parent.parent))

from lib.Array.arrays import groupAnagrams

def test_groupAnagrams():
    # Test case 1
    strs1 = ["eat", "ate", "tan", "nat", "can"]
    result1 = groupAnagrams(strs1)
    assert result1 == [['eat', 'ate'], ['tan', 'nat'], ['can']]

    # Test case 2 (add more test cases as needed)
    strs2 = ["listen", "silent", "enlist"]
    result2 = groupAnagrams(strs2)
    assert result2 == [['listen', 'silent', 'enlist']]

# Add more test cases and functions if needed