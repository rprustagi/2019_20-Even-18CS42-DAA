#program to generate input for Q01.
import sys
import random
from datetime import date
from datetime import datetime

if len(sys.argv) !=2:
  print("Usage: ", sys.argv[0], "<number>")
  exit()
num = int(sys.argv[1])

st=date.today().replace(day=1, month=1, year=1970).toordinal()
et=date.today().toordinal()
arr = [date.fromordinal(random.randint(st,et)).strftime("%Y-%m-%d") for i in range(num)]

of = open("Q07.inp","w+")

of.write("\n".join([str(ele) for ele in arr]))
of.write("\n")
of.close()

