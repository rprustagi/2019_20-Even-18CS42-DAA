# generate harmonic series first N terms and their sum
import sys
import math

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
print("Harmonic series for", number, "terms are:")
print("1/1", end=" ")
sum=1.0
for ii in range(2, number + 1):
  print(" + 1/" + str(ii), end="")
  sum = sum + 1 / ii
print("")
print("Sum of harmonic series = ", sum)
exit()
