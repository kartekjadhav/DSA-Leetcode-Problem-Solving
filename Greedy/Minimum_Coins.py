# !!!! This greedy solution is only valid when sum of previous elements is not greater than their next elements.
# e.g Valid case - [1, 2, 5, 10, 20, 50, 100, 500, 1000] where V = 49
# e.g Invalid Case - [1, 5, 6, 9] where V = 11 and here 5 + 6 is greater than their next element 9

#TC - O(V) (If all coins is 1)
#SC - O(1)

def mininumCoins(arr: int, value: int ) -> int:
    res = sorted(arr)
    i = len(arr) - 1
    coins = 0
    while i>=0 and value>0:
        if arr[i] > value:
            i-=1
        else:
            value -= arr[i]
            coins += 1
    return coins

arr = [1, 2, 5, 10, 20, 50, 100, 500, 1000]
value = 49
ans = mininumCoins(arr, value)
print(ans)