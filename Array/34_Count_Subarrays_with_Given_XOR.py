#TC - O(N), SC - O(N)
def subarraysXor(arr, x):
    # Write your code here
    # Return an integer
    hashmap = {0:1}
    count = 0
    prefixXor = 0
    for i in range(len(arr)):
        prefixXor ^= arr[i]
        temp = prefixXor ^ x
        if temp in hashmap:
            count += hashmap[temp]
        hashmap[prefixXor] = 1 + hashmap.get(prefixXor, 0)

    return count