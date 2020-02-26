#program to generate input for Q01.
import sys
import random
from datetime import date
from datetime import datetime

if len(sys.argv) !=2:
  print("Usage: ", sys.argv[0], "<number>")
  exit()
num = int(sys.argv[1]) # number of characters in a string

arr = [chr(random.randint(97,122)) for i in range(num)]

of = open("Q08.inp","w+")

of.write("".join([str(ele) for ele in arr]))
of.write("\n")
of.close()

