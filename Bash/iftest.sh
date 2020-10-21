#!/bin/bash
echo -n "$:"
read x
if [ $x -eq "help"]
	then
		echo "copyterm v1"
	else
		echo "q"
fi
