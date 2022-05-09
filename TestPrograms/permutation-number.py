# generate all possible permutations of a given number (less than 10)
import sys

def permutation(elems, str):
  #print("elems=", elems, "str = ", str)
  if (len(elems) <= 1):
    print(str + elems[0])
    return
  for i in range(len(elems)):
    subelems = elems.copy()
    subelems.remove(elems[i])
    permutation(subelems, str + elems[i])

# validation checks
if (len(sys.argv) != 2):
  print("Usage: ", sys.argv[0], "<number between 1 and 9>")
  exit()

try:
  number = int(sys.argv[1])
except:
  print("Invalid input")
  exit()
if (number >9) or (number < 0):
  print("Input", number, "not between 1 and 9.")
  exit()

# main program
elems = []
for i in range(1, number + 1):
  elems.append(str(i))
permutation(elems, "")
exit()
