def mergeSort(arr):
    if len(arr) > 1:
  
        mid = len(arr)//2
  
        L = arr[:mid]
        R = arr[mid:]

        mergeSort(L)
        mergeSort(R)
        
        i = j = k = 0
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if int(str(L[i])+str(R[j]))>int(str(R[j])+str(L[i])): #checking by string concat instead
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
  
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
  
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

for _ in range(int(input())):
      n=int(input())
      arr = list(map(int,input().split()))
      mergeSort(arr)
      print("".join(list(map(str,arr))))
