#!/bin/bash

set -u


if [[ $# -lt 1 ]]; then
        printf "Usage: %s FILE [NUM]\n" "$(basename "$0")"
        exit 1
fi

if [[ ! -f $1 ]]; then
        printf "%s is not a file" \"$1\"
        exit 1
fi


FILE=$1
NUM=${2:-"3"}
i=0

while read -r LINE; do
	let i++
	if [[ $i -le $NUM ]]; then
		printf "%s\n" "$LINE"
	
	elif [[ $i -gt $NUM ]]; then
	break
fi

done < "$FILE"
