#Note - Use DisjointSet template from DisjointSet.py file in this list

#TC - O(N*M) 
#WHERE N IS SIZE LEN(ACCOUNTS) AND M IS MAX SIZE OF ACCOUNTS[I]
from typing import List
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        n = len(accounts)
        dsj = DisjointSet(n) # type: ignore
        hashmap = {}
        for i in range(n):
            for j in range(1,len(accounts[i])):
                mail = accounts[i][j]
                if mail in hashmap:
                    dsj.unionSize(i,hashmap[mail])
                else:
                    hashmap[mail] = i

        hashresult = {}
        for key,value in hashmap.items():
            res = dsj.findPar(value)
            if res not in hashresult:
                hashresult[res] = [accounts[res][0],key]
            else:
                hashresult[res].append(key)
        
        ans = []
        for arr in hashresult.values():
            arr[1:] = sorted(arr[1:])
            ans.append(arr)
        return ans