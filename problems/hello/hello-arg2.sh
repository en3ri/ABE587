#!/bin/bash

if [[ $# -lt 2 ]]; then
	printf "Usage: %s GREETING NAME\n" "$(basename "$0")"
	exit 1
fi

GREETING=$1
NAME=$2

echo "$GREETING, $NAME"!
