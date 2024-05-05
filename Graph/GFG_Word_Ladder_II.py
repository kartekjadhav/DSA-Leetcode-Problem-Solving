from collections import deque
class Solution:
    def findSequences(self, startWord, targetWord, wordList):
        #Code here
        wordset = set()
        for i in wordList:
            wordset.add(i)
        ans = []
        q = deque()
        q.append([startWord])
        if startWord in wordset:
            wordset.remove(startWord)
        while q:
            tempList = q.popleft()
            word = tempList[-1]
            
            #removing words from wordList
            if word in wordset:
                wordset.remove(word)
            
            # If we get targetWord add in ans list if 
            # it's len is equal to shortest ans list possible i.e ans[0]
            if word==targetWord and not ans:
                ans.append(tempList)
            elif word==targetWord and len(tempList)==len(ans[0]):
                ans.append(tempList)
            
                
            #Forming all possible words 
            for i in range(len(word)):
                for j in range(26):
                    new_word = word[:i] + chr(97+j) + word[i+1:]
                    if new_word in wordset:
                        tempList.append(new_word)
                        q.append(tempList[:])
                        tempList.pop()
        return ans