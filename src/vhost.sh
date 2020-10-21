#!/bin/bash
dir_script=$(dirname "$0")
root_project=$(pwd)
sudo python3 "${dir_script}/vhost.py" -r $root_project
