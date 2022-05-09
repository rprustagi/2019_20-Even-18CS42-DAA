# generate all prime factors of a given number
import sys

# validation checks
if (len(sys.argv) != 3):
  print("Usage: ", sys.argv[0], "string", "<rotate value>")
  exit()

try:
  arr = list(sys.argv[1])
  rotateleft = int(sys.argv[2])
except:
  print("Invalid input")
  exit()
if (rotateleft < 0):
  print("Input", number, "not a positive number.")
  exit()

# write a reverse function
def reverse(arr, i, j):
  # reverse list starting from index i to j(inclusive)
  mid = (j - i + 1) // 2
  for k in range(mid):
    arr[i+k], arr[j-k] = arr[j-k], arr[i+k]

# main program
print("Input array is", arr)
reverse(arr, 0, rotateleft-1)
reverse(arr, rotateleft, len(arr)-1)
reverse(arr, 0, len(arr)-1)
print("Rotated array is", arr)
exit()
