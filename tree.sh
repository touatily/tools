#!/bin/bash

function tr() {
# $1 is the directory
# $2 is the ident

echo "$2$1"	
local i=" == $2"
l=$(ls $1)
for f in $l; do
	if [ -d "$1/$f" ]; then
		tr "$1/${f}" "${i}"
	else
		echo "${i}${f}"
	fi 
done
}

if [ $# -eq 1 ]; then
	d=$1
else
	d="."
fi

tr $1 ""
