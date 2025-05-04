#!/bin/bash

script_dir="$(dirname "$(realpath "$BASH_SOURCE")")"

file="$script_dir/server.config"
word="path"

grep "^$word:" "$file"
