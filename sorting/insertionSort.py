# 2 - Insertion Sort
myList = [1, 9, 3, 5, 2, 10, 4]

def insertionSort(a):
  length = len(a)
  i = 1
  while(i < length):
    j = i - 1
    temp = a[i]
    while(j >= 0 and a[j] > temp):
      a[j+1] = a[j]
      j = j - 1
    a[j + 1] = temp
    i = i + 1

print(myList)
print("After insertion Sort")
insertionSort(myList)
print(myList)
