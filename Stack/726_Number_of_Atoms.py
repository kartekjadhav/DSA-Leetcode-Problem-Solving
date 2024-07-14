class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = [{}]
        i = 0

        while i<len(formula):
            s = formula[i]
            if s=='(':
                stack.append({})
            elif s==')':
                count = ''
                while i+1<len(formula) and formula[i+1].isdigit():
                    count += formula[i+1]
                    i+=1
                count = 1 if not count else int(count)
                for key in stack[-1].keys():
                    stack[-1][key] *= count
                hashmap = stack.pop()
                for key,val in hashmap.items():
                    if key in stack[-1]:
                        stack[-1][key] += val
                    else:
                        stack[-1][key] = val
            else:
                element = formula[i]
                if i+1<len(formula) and formula[i+1].islower():
                    element = formula[i:i+2]
                    i+=1
                count = ''
                while i+1<len(formula) and formula[i+1].isdigit():
                    count += formula[i+1]
                    i+=1
                count = 1 if not count else int(count) 
                stack[-1][element] = count + stack[-1].get(element,0)
            i+=1
            
        
        hashmap = stack.pop()
        ans = ''
        for key in sorted(hashmap.keys()):
            if hashmap[key]>1:
                ans = ans + key + str(hashmap[key])
            else:
                ans = ans + key
        return ans