# Bubble Sort
def bubble_sort(a):
  length = len(a)
  i = 0
  while( i < length - 1):
    j = 0
    while( j < length - 1 - i):
      if(a[j] > a[j + 1]):
        temp = a[j]
        a[j] = a[j+1]
        a[j + 1] = temp
        j = j + 1
    i = i + 1
    
# insertion Sort
def insertionSort(a):
  length = len(a)
  i = 1
  while( i < length):
    j = i - 1
    temp = a[i]
    while(j >= 0 and a[j] > temp):
      a[j + 1] = a[j]
      j = j - 1
    # At this point we'll have the location where to insert
    a[j + 1] = temp
    i = i + 1
