#!/usr/bin/env python3

import os
import sys
import re

script_dir = os.path.dirname(os.path.realpath(__file__))

FILE = os.path.join(script_dir, "server.config")
WORD = "path"

if not os.path.isfile(FILE):
  print("\033[31mError: File \"{}\" not found\033[0m".format(FILE))
  sys.exit(1)

try:
  with open(FILE, "r") as f:
    for line in f:
      if re.search(r"^" + re.escape(WORD) + r":", line):
        print(line.strip())
except Exception as e:
  print("\033[31mError: Unable to read file {}\033[0m".format(e))
  sys.exit(1)
