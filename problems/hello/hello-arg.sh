#!/bin/bash

if [[ $# -lt 1 ]]; then
	printf "Usage: %s name\n" "$(basename "$0")"
	exit 1
fi

echo "Hello, $1"!
