#   arg1: filename containing elements (string) to be sorted
import sys

def merge(A,  B):
  # It is assumed that two arrays are divisions of a single array
  # and thus first element of B starts after the last elment of A
  # in the largerm combined array
  # after the merge operation, all elements of A will be less than that of B.
  lena = len(A)
  lenb = len(B)
  aa = 0
  bb = 0

  print("Arrays to merge in place are", A, B)

  while ((aa < lena) and (bb < lenb)):
    if B[bb] < A[aa]:
      A[aa],B[bb] = B[bb], A[aa] # swap operation
      bb = bb + 1
    else:
      A.append(C[cc])
      cc = cc + 1
  print("indexes are bb=", bb, "cc=", cc, "A=", A)
  if (bb >= lenb):
    for j in range(cc,lenc):
      print("j=", j, C[j])
      A.append(C[j])
  else:
    for i in range(bb, lenb):
      print("i=", i, B[i])
      A.append(B[i])
  print("Merged", B, "and", C, "into", A)
  return

def mergesort(Arr):
  #print("i/p:", Arr)
  size = len(Arr)
  if size > 1:
    B = Arr[0:size//2]
    C = Arr[size//2:]
    #print("two sub arrays are", B, C)
    mergesort(B)
    mergesort(C)
    Arr.clear()
    merge(B, C, Arr)
    print("Merged", B, "and", C, "into", Arr)
  else:
    print("Input array", Arr, "is small and sorted")
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

mergesort(data)

exit()

