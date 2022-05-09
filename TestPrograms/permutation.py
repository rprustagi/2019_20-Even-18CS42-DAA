# generate all possible permutations of a given number (less than 10)
import sys

def permutation(elems, list):
  if (len(elems) <= 1):
    #print(list + elems)
    for x in list + elems:
      print(x, end=" ")
    print("")
    return
  for i in range(len(elems)):
    subelems = elems.copy()
    subelems.remove(elems[i])
    permutation(subelems, list + [elems[i]])

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
elems = []
for i in range(0, number):
  elems.append(chr(ord('A')+i))
permutation(elems, [])
exit()
