import os
import sys
import time

# validation checks
if (len(sys.argv) < 2):
  print("Usage: ", sys.argv[0], "<cmd1> <cmd2> ...")
  exit()

cmd_num = 1
while (cmd_num < len(sys.argv)):
  cmd=sys.argv[cmd_num]
  print("Executive command '" + cmd + "'")
  time.sleep(2)
  os.system(cmd)
  cmd_num = cmd_num + 1

print("All", cmd_num, "commands are executed")
