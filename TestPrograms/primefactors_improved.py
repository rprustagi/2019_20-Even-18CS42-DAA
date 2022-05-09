# generate all prime factors of a given number
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
print("prime factors of", number, "are:")
for factor in range(2, int(math.sqrt(number)) + 1):
  #print(factor)
  while number % factor == 0:
    print(factor, end=" ")
    number = number // factor
if number > 1:
  print(number)
else:
  print("")
exit()
