
from collections import deque


class Solution:
    #Brute Force by stack
    #TC - O(N^2), SC - O(N)
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        stack = []
        i = 0
        q = deque()
        while i<n:
            if s[i]==')': 
                while stack[-1]!='(': q.append(stack.pop())
                stack.pop()
                while q: stack.append(q.popleft())
            else:
                stack.append(s[i])
            i+=1
        return "".join(stack)
    
    #Optimizing stack approach
    #TC - O(N^2), SC - O(N)
    def reverseParentheses(self, s: str) -> str:
        def reverse(i,j):
            while i<j:
                ds[i], ds[j] = ds[j], ds[i]
                i+=1
                j-=1
        
        ds = []
        stack = []
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(len(ds))
            elif s[i]==')':
                start = stack.pop()
                end = len(ds)-1
                reverse(start, end)
            else:
                ds.append(s[i])
        
        return "".join(ds)
    

    #Wormhole Teleportation Technique
    #TC - O(N), SC - O(N)
    def reverseParentheses(self, s: str) -> str:
        n = len(s)
        stack = []
        hashing = [-1]*n
        #Forming Hashing array
        for i in range(n):
            if s[i]=='(':
                stack.append(i)
            elif s[i]==')':
                temp = stack.pop()
                hashing[temp] = i
                hashing[i] = temp
        
        direction = 1
        i = 0
        ds = []
        while i<n:
            if s[i]=='(' or s[i]==')':
                i = hashing[i]
                direction *= -1
            else:
                ds.append(s[i])
            i+=direction

        return "".join(ds)