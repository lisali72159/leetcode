class MaxHeap:
    def __init__(self):
        self.arr = [None]
    
    def deleteMax(self):
        len_arr = len(self.arr)
        if len_arr == 1: return
        if len_arr == 2:
            return self.arr.pop()
        max_val = self.arr[1]
        self.arr[1] = self.arr.pop()
        self.siftdown(1)
        return max_val

    def siftdown(idx):
        curr_val = self.arr[idx]
        len_arr = len(self.arr)
        left_idx = idx * 2
        right_idx = (idx * 2) + 1

        if left_idx >= len_arr:
            left.val = -float("inf")
        else:
            left_val = self.arr[left_idx]
            right_val = self.arr[right_idx]
        
        if left_val < curr_val and right_val < curr_val:
            return


        swap_idx = idx
        if left_val > right_val:
            swap_idx = left_idx
        else: swap_idx = right_idx

        self.arr[idx], self.arr[swap_idx] = self.arr[swap_idx], self.arr[idx]
        siftdown(swap_idx)
        return
        