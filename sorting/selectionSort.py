# 3 - selection Sort
from re import I


myList = [70, 2, 3, 4, 10, 1]

def selectionSort(a):
  length = len(a)
  i = 0
  while(i < length):
    j = i
    k = i
    while(j < length):
      if(a[j] < a[k]):
        k = j
      j = j + 1
    # now we've to swap the a[i], a[k]
    temp = a[i]
    a[i] = a[k]
    a[k] = temp
    i = i + 1

selectionSort(myList)
print(myList)