#!/bin/bash
dir_script=$(dirname "$0")
root_project=$(pwd)
sudo python3 "${dir_script}/main.py" -r $root_project
