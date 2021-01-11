from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> str:
        counter = Counter()
        for i in s:
            counter.update(i)
        for item,count in counter.items():
            if count==1:
                return item
        return " "

class Solution2:
    def firstUniqChar(self, s: str) -> str:
        dicts={}
        for i in s:
            dicts[i]=dicts.get(i,0)+1
        for i in s:
            if dicts[i]==1:
                return i
        return ' '

from collections import defaultdict
class Solution3:
    def firstUniqChar(self, s: str) -> str:
        _dict = defaultdict(bool)
        for i in s:
            _dict[i] = not i in _dict
        for i in s:
            if _dict[i]==True:
                return i
        return ' '
