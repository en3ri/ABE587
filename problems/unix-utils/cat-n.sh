#!/bin/bash

set -u


if [[ $# -lt 1 ]]; then
	printf "Usage: %s file\n" "$(basename "$0")"
	exit 1

elif [[ ! -f $1 ]]; then
	printf "%s is not a file" \"$1\"
	exit 1
fi

i=0
FILE=$1
while read -r LINE; do
	let i++
	printf "%3d %s\n" $i "$LINE"
done < "$FILE"
