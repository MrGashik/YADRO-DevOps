#!/bin/bash

file=""
word=""

while getopts "f:w:h" opt; do
  case $opt in
    f) file="$OPTARG" ;;
    w) word="$OPTARG" ;;
    h) echo "Using: $0 -f \"<path_file>\" -w \"<word>\""
       echo "flags:"
       echo -e "\t-f: Specifies the path to the file. Example: -f \"/path/to/file/file.*\""
       echo -e "\t-w: Specifies search word. Example: -w \"word\""
       exit 1 ;;
    ?) echo -e "\e[31mUsing: $0 -f <path_file> -w <word>\e[0m"
       exit 0 ;;
  esac
done

if [ -z "$file" ] || [ -z "$word" ]; then
  echo -e "\e[31mError: Specify file path and search word\e[0m"
  exit 1
fi

if [ ! -f "$file" ]; then
  echo -e "\e[31mError: File \"$file\" not found\e[0m"
  exit 1
fi

grep -w "^$word:" "$file"
