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

def remove(arr):
  num = len(arr)
  # remove some random number of elements from array
  rnd = random.randint(1, num // 2)
  for i in range(rnd):
    x=arr.pop(random.randint(0, num - i - 1))

arr1 = [i for i in range(1, num1 + 1)]
arr2 = [i for i in range(1, num2 + 1)]

remove(arr1)
remove(arr2)

writedata("Q04a.inp", arr1)
writedata("Q04b.inp", arr2)

