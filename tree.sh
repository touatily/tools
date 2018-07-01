#!/bin/bash

function tr() {
	# $1 is the directory
	# $2 is the ident


	f=`basename $1`
	s=`du -sh $1 | cut -f -1`
	echo -e "[${s}]\t$2$f"


	local i="    $2"
	l=$(ls $1)


	for f in $l; do
		if [ -d "$1/$f" ]; then
			tr "$1/${f}" "${i}"
		else
			file=`basename $f`
			s=`du -sh "$1/$f" | cut -f -1`
			echo -e "[${s}]\t${i}${file}"
		fi 
	done
}

if [ $# -eq 1 ]; then
	d=$1
else
	d="."
fi

tr $d ""
