#   arg1: filename containing elements (string) to be sorted
import sys

def swap(i, j, arr):
  temp = arr[i]
  arr[i] = arr[j]
  arr[j] = temp

def partition(left, right, arr):
  pivot = arr[right]
  i = left
  j = right - 1
  while (i <= j):
    # find first element greater than pivot from left
    while arr[i] <= pivot and (i < right):
      i = i + 1
    if (i == right): # all elements are smaller than pivot
      return right
    # find first element smaller than pivot right
    while (j >= left) and (arr[j] > pivot):
      j = j - 1
    if (j < left): # all elements are bigger than pivot
      arr[left], arr[right] = arr[right], arr[left]
      return left
    if (i < j): #swap low and high and continue
      arr[i], arr[j] = arr[j], arr[i]
    # end while (i<=j)
  arr[i], arr[right] = arr[right], arr[i]
  return i

def quicksort(left, right, arr):
  if left < right:
    s = partition(left, right, arr)
    quicksort(left, s-1, arr)
    quicksort(s+1, right, arr)
  return

# validation checks
#sys.argv = ["qsort.py", "data2.txt"]
if (len(sys.argv) != 2):
  print("Usage: ", sys.argv[0], "<file with elements>")
  exit()
datafile = sys.argv[1]
try:
  fhdata = open(datafile)
except:
  print("Data file does not exist")
  exit()

# main program
data = []
for line in fhdata:
  line = line.strip()
  for word in line.split():
    data.append(word)
origdata = data.copy()
#print("input: ", origdata)
quicksort(0, len(data)-1, data)
 print("output: ", data)

# verify if the data is actually sorted.
sortdata = data.copy()
data.sort()
if (sortdata != data):
  print("Quick sort failed for ", origdata)
else:
  print("Quick sort successful for", origdata)

exit()

