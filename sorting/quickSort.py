# 4 - QuickSort

myList = [1, 3, 10, 2, 19, 14, 8]

def partition(arr, low, high):
  pivot = arr[high]
  i = low - 1
  for j in range(low, high):
    if arr[j] <= pivot:
      i = i + 1
      arr[i], arr[j] = arr[j], arr[i]
  arr[i + 1], arr[high] = arr[high], arr[i + 1]
  return i + 1

def quickSort(arr,low, high):
  if low < high:
    p = partition(arr, low, high)
    quickSort(arr, low, p - 1)
    quickSort(arr, p + 1, high)

print(myList)
print("After Sorting")
quickSort(myList, 0, len(myList) - 1)
print(myList)