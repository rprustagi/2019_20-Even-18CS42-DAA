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
if (number < 2):
  print("Input", number, "number should be >2.")
  exit()

# main program
print("First", number, "terms of Fibonacci series starting from 1, 1 are")
prev = 1
curr = 1
print("1, 1", end="")
while number > 2:
  sum = prev + curr
  prev = curr
  curr = sum
  number = number - 1
  print(",", sum, end="")
print("")
exit()
