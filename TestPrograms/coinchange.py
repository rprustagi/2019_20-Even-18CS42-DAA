# generate coin change count
import sys

# global variables
denomination = [1,2,5,10,20,25]
res = [0] * len(denomination)
def coinchange(amt):
  global cnt
  index=len(denomination) - 1
  while (index >=0):
    while(amt >= denomination[index]):
      res[index] = res[index] + 1
      amt = amt - denomination[index]
      cnt = cnt + 1
    index = index - 1

# validation checks
if (len(sys.argv) != 2):
  print("Usage: ", sys.argv[0], "<amount>")
  exit()

try:
  amt = int(sys.argv[1])
except:
  print("Invalid input")
  exit()
if (amt < 0):
  print("Input", amt, "not a positive value.")
  exit()

cnt = 0
coinchange(amt)
print("Total", cnt, "coins needed for the amount", amt)
for i in range(len(res)-1, -1, -1):
  if (res[i] != 0):
    print("Coins for denomination", denomination[i], "=", res[i])

