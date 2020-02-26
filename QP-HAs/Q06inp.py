#program to generate input for Q01.
import sys
import random

if len(sys.argv) !=2:
  print("Usage: ", sys.argv[0], "<number>")
  exit()
num = int(sys.argv[1])
of = open("Q06.inp","w+")
arr = [random.randint(-num, num) for i in range(num)]

of.write("\n".join([str(ele) for ele in arr]))
of.write("\n")
of.close()

