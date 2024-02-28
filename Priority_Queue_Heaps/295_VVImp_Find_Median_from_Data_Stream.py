import heapq

#Solution 1 -> Using Insertion sort
class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        i = len(self.arr)-1
        j = i-1
        while j>=0:
            if self.arr[j]>self.arr[i]:
                self.arr[j],self.arr[i] = self.arr[i],self.arr[j]
                i-=1
                j-=1
            else: break

    def findMedian(self) -> float:
        n = len(self.arr)
        result = 0
        if n%2==0:
            result = (self.arr[n//2] + self.arr[n//2 - 1]) / 2
        else:
            result = self.arr[n//2]/1
        return result
    
#Solution 2 -> Using Heaps
class MedianFinder:

    def __init__(self):
        #small -> maxheap , large -> minheap
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small,-num)
        if len(self.large)>0 and -self.small[0] > self.large[0]:
            temp = -heapq.heappop(self.small)
            heapq.heappush(self.large, temp)
        
        s,l = len(self.small), len(self.large)
        if abs(s-l)>1:
            if s>l:
                heapq.heappush(self.large,-1*heapq.heappop(self.small))
            else:
                heapq.heappush(self.small,-1*heapq.heappop(self.large))

    def findMedian(self) -> float:
        s,l = len(self.small), len(self.large)
        if s>l:
            return -self.small[0]/1
        elif l>s:
            return self.large[0]/1
        else: return (-self.small[0] + self.large[0])/2