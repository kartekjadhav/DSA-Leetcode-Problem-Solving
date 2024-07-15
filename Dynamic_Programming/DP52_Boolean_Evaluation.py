#TC - O(N*N*N*2), SC - extra space - O(N*N*2), stack space - O(N)
def evaluateExp(exp: str) -> int:
    # Write your code here.
    mod = 1000000007
    def dfs(i,j,isTrue):
        #Base Case
        if i > j:
            return 0
        if i == j:
            if isTrue == 1:
                return 1 if exp[i] == 'T' else 0
            else:
                return 1 if exp[i] == 'F' else 0
        if dp[i][j][isTrue]!=-1: return dp[i][j][isTrue]

        count = 0        
        for ind in range(i+1, j, 2):
            lT = dfs(i, ind-1, 1)
            lF = dfs(i, ind-1, 0)
            rT = dfs(ind+1, j, 1)
            rF = dfs(ind+1, j, 0)

            if exp[ind]=='&':
                if isTrue==1:
                    count += (lT*rT)%mod
                else:
                    count += ((lT*rF)%mod + (lF*rT)%mod + (lF*rF)%mod)%mod
            
            elif exp[ind]=='|':
                if isTrue==1:
                    count += ((lT*rF)%mod + (lF*rT)%mod + (lT*rT)%mod)%mod
                else:
                    count += (lF*rF)%mod

            elif exp[ind]=='^':
                if isTrue==1:
                    count += ((lT*rF)%mod + (lF*rT)%mod)%mod
                else:
                    count += ((lT*rT)%mod + (lF*rF)%mod)%mod

        count%=mod
        dp[i][j][isTrue] = count
        return dp[i][j][isTrue]

    dp = [[[-1]*2 for _ in range(len(exp))] for _ in range(len(exp))]
    return dfs(0,len(exp)-1,1)