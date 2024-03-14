class Item:
    def __init__(self,val,w):
        self.value = val
        self.weight = w
        
class Solution:    
    #Function to get the maximum total value in the knapsack.
    def fractionalknapsack(self, W,arr,n):
        
        # code here
        sorted_arr = sorted(arr, key=lambda x: x.value/x.weight, reverse=True)
        
        profit, currWeight = 0.0, 0.0
        
        for item in sorted_arr:
            if W >= currWeight + item.weight:
                currWeight += item.weight
                profit += item.value
            
            else:
                valueByweight = item.value / item.weight
                remain = W - currWeight
                profit += valueByweight * remain
                break
        
        return profit