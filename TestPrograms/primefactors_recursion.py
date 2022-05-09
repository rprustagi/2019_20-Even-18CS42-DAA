# generate all prime factors of a given number
import sys

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

def prime(n):
  #print("n = ", n)
  for factor in range(2, n + 1):
    #print("factor = ", factor)
    if (n % factor) == 0:
      print(factor, end=" ")
      prime(n // factor)
      break
  return

# main program
print("prime factors of", number, "are:")
prime(number)
print("")
exit()
