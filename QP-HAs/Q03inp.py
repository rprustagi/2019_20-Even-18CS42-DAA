#!/usr/bin/env python
import sys
import random

#sys.argv = ["prg.py", 1000, 2000]
if len(sys.argv) !=3:
  print("Usage: ", sys.argv[0], "<number-1> <number-2")
  exit()
num1 = int(sys.argv[1])
num2 = int(sys.argv[2])

def writedata(filename, arr):
  #write the data
  of = open(filename,"w+")
  of.write("\n".join([str(ele) for ele in arr]))
  of.write("\n")
  of.close()
  return

def remove_and_dup(arr):
  num = len(arr)
  # remove some random number of elements from array
  rnd = random.randint(1, num // 2)
  #print(num, rnd)
  for i in range(rnd):
    x=arr.pop(random.randint(0, num - i - 1))
    #print("popped out ", x)
  #print(arr)
  lenarr = num - rnd
  # determine count of numbers to be repeated
  rnd = random.randint(0, lenarr // 2)
  #print("num of elems to repeat", rnd)
  for i in range(rnd): # for each such value to be repeted
    numdup = random.randint(1,10) # at most 10 repetitions
    idx = random.randint(0,lenarr + i - 1)
    #print("element at idx", idx, "value", arr[idx], "to be repeated", numdup, "times")
    dup = arr[idx] # the value of number to be repeated
    for j in range(numdup):
      arr.insert(idx, dup)
    #print(arr)

arr1 = [i for i in range(1, num1 + 1)]
arr2 = [i for i in range(1, num2 + 1)]

remove_and_dup(arr1)
remove_and_dup(arr2)

writedata("Q03a.inp", arr1)
writedata("Q03b.inp", arr2)

