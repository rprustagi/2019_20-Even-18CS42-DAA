import sys

def octal(num):
  if num < 8:
    return str(num)
  else:
    return octal(num//8) + str(num %8)
#
N = int(sys.argv[1])
print(octal(N))
