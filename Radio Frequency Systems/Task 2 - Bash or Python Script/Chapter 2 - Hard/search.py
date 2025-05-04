#!/usr/bin/env python3

import os
import sys
import re

file = ""
word = ""

if len(sys.argv) > 5:
  print("\033[31mError: Many parameters")
  print("\tUse {} -h for help\033[0m".format(sys.argv[0]))
  sys.exit(1)

for i in range(1, len(sys.argv), 2):
  if (sys.argv[i] == "-f") and (i + 1 < len(sys.argv)):
    file = sys.argv[i + 1]
  elif (sys.argv[i] == "-w") and (i + 1 < len(sys.argv)):
    word = sys.argv[i + 1]
  elif sys.argv[i] == "-h":
    print("Using: {} -f \"<path_file>\" -w \"<word>\"".format(sys.argv[0]))
    print("flags:")
    print("\t-f: Specifies the path to the file. Example: -f \"/path/to/file/file.*\"")
    print("\t-w: Specifies search word. Example: -w \"word\"")
    sys.exit(0)
  elif ((sys.argv[i] == "-f") or (sys.argv[i] == "-w")) and (i + 1 >= len(sys.argv)):
    print("\033[31mError: Empty parameter {}\033[0m".format(sys.argv[i]))
    sys.exit(1)
  else:
    print("\033[31mError: Unknows parameter {}\033[0m".format(sys.argv[i]))
    sys.exit(1)

if (file == "") or (word == ""):
  print("\033[31mError: Specify file path and search word\033[0m")
  sys.exit(1)

if not os.path.isfile(file):
  print("\033[31mError: File \"{}\" not found\033[0m".format(file))
  sys.exit(1)

try:
  with open(file, "r") as f:
    for line in f:
      if re.search(r"^" + re.escape(word) + r":", line):
        print(line.strip())
except Exception as e:
  print("\033[31mError: Unable to read file {}\033[0m".format(e))
  sys.exit(1)
