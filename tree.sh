#!/bin/bash


help="$0 is an alternative of the tree command \n\
Usage:\n\
\t$0 [-f file or directory] [-i ident] [-d deth] \n\
\t$0 [-h]"


file="."
ident="    "

while getopts ":f:i:d:h:" opt; do
  case $opt in
    f)
      file=$OPTARG
      ;;
    d)
      deth=$OPTARG
      ;;
    h)
      echo -e $help
      exit 1
      ;;
    i)
      ident=$OPTARG
      ;;
    *)
      echo -e "$help"
      exit 1
      ;;
  esac
done



function tr() {
	# $1 is the directory
	# $2 is the ident


	f=`basename $1`
	s=`du -sh $1 | cut -f -1`
	echo -e "[${s}]\t$2$f"


	local i="$ident$2"
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



tr $file "$ident"
