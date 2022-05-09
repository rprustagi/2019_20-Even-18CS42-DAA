# generate harmonic series first N terms and their sum
import sys
import math

#sys.argv=["abc", 10]
# validation checks
if (len(sys.argv) != 2):
  print("Usage: ", sys.argv[0], "<number>")
  exit()

try:
  number = int(sys.argv[1])
except:
  print("Invalid input")
  exit()
if (number < 0):
  print("Input", number, "not a positive number.")
  exit()

# main program
print("Binary representation for", number, "is:")
binstr = ""
while number > 0:
  remainder = number % 2
  binstr = str(remainder) + binstr
  number = number // 2
print(binstr)

exit()
