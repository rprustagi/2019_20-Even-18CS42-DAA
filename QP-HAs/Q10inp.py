#program to generate input for Q01.
import sys
import random

if len(sys.argv) !=2:
  print("Usage: ", sys.argv[0], "<number>")
  exit()
num = int(sys.argv[1])
of01 = open("Q10.inp","w+")
arr = [i for i in range(1, num+1)]
numtoadd = random.randint(1,num-1)
print("number duplicated is", numtoadd)
arr.insert(numtoadd, arr[numtoadd])
random.shuffle(arr)
of01.write("\n".join([str(ele) for ele in arr]))
of01.write("\n")
of01.close()

