from exceptions import HeapError, HeapEmptyError, InvalidHeapKvalue
class Minheap:
    # Initializing heap with a empty list and a counter to keep track of insertion counter
    def __init__(self):
        self.heap = []
        self.counter = 0

    # Method to find the parent of a node at i
    def parent(self, i):
        return (i - 1) // 2

    # Pushing entry obj with parameters key, obj and adding a self.counter variable to it for tie-breaker if keys are equal
    def push(self, key, obj):
        entry = (key, obj, self.counter)
        self.heap.append(entry)
        i = len(self.heap) - 1
        while i != 0 and (self.heap[self.parent(i)][0], self.heap[self.parent(i)][2]) > (self.heap[i][0], self.heap[i][2]):
            self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
            i = self.parent(i)
        self.counter += 1

    # Popping and returning the obj with minimum key and restoring the heap
    # returning error if heap is empty and handling the case when heap has only 1 element in it
    def pop(self):
        if len(self.heap) == 0:
            raise HeapError("Heap Error")

        if len(self.heap) == 1:
            return self.heap.pop()[1]

        self.heap[0], self.heap[len(self.heap) - 1] = self.heap[len(self.heap) - 1], self.heap[0]
        ele = self.heap.pop()[1]
        n = len(self.heap)

        i = 0

        while True:
            left = 2*i + 1
            right = 2*i + 2
            smallest = i

            if left < n and (self.heap[left][0], self.heap[left][2]) < (self.heap[smallest][0], self.heap[smallest][2]):
                smallest = left

            if right < n and (self.heap[right][0], self.heap[right][2]) < (self.heap[smallest][0], self.heap[smallest][2]):
                smallest = right

            if smallest == i:
                break

            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest

        return ele

    # Returning the obj with smallest key without removing it and raising Exception if heap is empty
    def peek(self):
        if len(self.heap) == 0:
            raise HeapEmptyError("Heap Empty")

        return self.heap[0][1]

    # Returning K objects with smallest keys and raising error if k is less than -1
    # If k is -1 or greater than equal to nnumber of elements in heap we return all the objects hence we set k to n
    # If k is 0 or heap is empty we return empty list
    def ksmallest(self, k):
        if k < -1:
            raise InvalidHeapKvalue("Cannot fetch K elements as K is invalid")

        n = len(self.heap)
        result = []

        if k == -1 or k >= n:
            k = n

        if k == 0 or n == 0:
            return result

        temp = Minheap()
        temp.push((self.heap[0][0], self.heap[0][2]), 0)

        while len(result) < k:
            _, i = temp.pop()
            result.append(self.heap[i][1])

            left = 2*i + 1
            right = 2*i + 2

            if left < n:
                key, _, count = self.heap[left]
                temp.push((key, count), left)

            if right < n:
                key, _, count = self.heap[right]
                temp.push((key, count), right) 

        return result

    # Defining heapify to create a heap from the list of items that are being provided and using sift_down 
    # as a helper function to make sure heap properties are followed
    @classmethod
    def heapify(cls, items):
        newHeap = cls()
        n = len(items)

        for i in range(n):
            newHeap.heap.append((items[i][0], items[i][1], i))
        newHeap.counter = n

        for i in range((n // 2) - 1, -1, -1):
            newHeap.sift_down(i)

        return newHeap

    def sift_down(self, i):
        n = len(self.heap)

        while True:
            left = 2*i + 1
            right = 2*i + 2
            smallest = i

            if left < n and (self.heap[left][0], self.heap[left][2]) < (self.heap[smallest][0], self.heap[smallest][2]):
                smallest = left

            if right < n and (self.heap[right][0], self.heap[right][2]) < (self.heap[smallest][0], self.heap[smallest][2]):
                smallest = right

            if smallest == i:
                break

            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            i = smallest

    def __len__(self):
        return len(self.heap)

    def __bool__(self):
        return len(self.heap) > 0

    def __repr__(self):
        return f"MinHeap(heap_length={len(self.heap)}, heap_counter={self.counter})"
    

