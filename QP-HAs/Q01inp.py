#program to generate input for Q01.
import sys
import random

if len(sys.argv) !=2:
  print("Usage: ", sys.argv[0], "<number>")
  exit()
num = int(sys.argv[1])
of01 = open("Q01.inp","w+")
arr = [i for i in range(1, num+1)]
numremove = random.randint(1,num)
print("number removed is", numremove)
arr.pop(numremove - 1)
random.shuffle(arr)
of01.write("\n".join([str(ele) for ele in arr]))
of01.write("\n")
of01.close()

