class Solution: 
    def select(self, arr, i):
        min_ele = arr[i]
        p1 = i
        while arr and i < len(arr):
            if min_ele > arr[i]:
                min_ele = arr[i]
                p1 = i
            i +=1
        # send the selected element attaching the it's index    
        return [p1,min_ele]
        # code here 
    
    def selectionSort(self, arr,n):
        k = 0
        while  k < n:
            sel = self.select( arr, k)
            #swap the two elements if the condition is satisfied
            if sel[1] < arr[k]:
                arr[k],arr[sel[0]] = arr[sel[0]],arr[k]
            k +=1
