# 1 - Bubble Sort
myList = [12, 45, 65, 49, 56, 1]

def bubbleSort(arr):
  length = len(arr)
  i = 0
  while(i < length - 1):
    j = 0
    flag = 0
    while(j < length - 1 - i):
      if(arr[j] > arr[j + 1]):
        # We'll swap the items
        temp = arr[j]
        arr[j] = arr[j + 1]
        arr[j + 1] = temp
        flag = 1
      j = j + 1
    i = i + 1

print(myList)
bubbleSort(myList)
print("After bubble sort!")
print(myList)