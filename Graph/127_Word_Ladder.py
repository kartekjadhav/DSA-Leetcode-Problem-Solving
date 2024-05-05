from typing import List
from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordset = set()
        for i in wordList:
            wordset.add(i)
        q = deque()
        q.append((beginWord,1))
        while q:
            word,level = q.popleft()
            if word==endWord: return level
            for i in range(len(word)):
                for j in range(26):
                    res = word[:i] + chr(97+j) + word[i+1:] 
                    if res in wordset:
                        q.append((res,level+1))
                        wordset.remove(res)
        return 0