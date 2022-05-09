#   arg1: filename containing elements (string) to be sorted
import sys

def swap(i, j, Arr):
  temp = Arr[i]
  Arr[i] = Arr[j]
  Arr[j] = temp

def partition(left, right, Arr):
  pivot = Arr[left]
  i = left + 1
  j = right
  while (i < j):
    while ((Arr[i] <= pivot) and (i < j)):
      i = i + 1
    while ((Arr[j] > pivot) and (j >= i)):
      j = j - 1
    swap(i, j, Arr)
  # end while
  swap(i, j, Arr) # undo the last swap
#  print("Undo swap:", Arr)
  swap(left, j, Arr)
  print("partition return = ", j, "Arr=", Arr)
  return j

def quicksort(left, right, arr):
  if left < right:
    s = partition(left, right, arr)
    quicksort(left, s-1, arr)
    quicksort(s+1, right, arr)
  return

# validation checks
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
data=[]
for line in fhdata:
  line = line.strip()
  data.append(line)

print("input: ", data)
quicksort(0, len(data)-1, data)
print("output: ", data)

exit()

