#!/bin/bash

if [ ! $# -gt 0 ]; then
	echo "Your command line contains $# arguments"
	exit 1
fi
if [ ! $# -gt 1 ]; then
	echo "Usage: uploadone.sh local_file remote_file"
	exit 1
fi


ampy -p $1 -b 115200 put $2 $3
ampy -p $1 -b 115200 get $3

