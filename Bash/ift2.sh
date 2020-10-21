#!/bin/bash
echo -n "num:";read USER_VAL;
if [ $USER_VAL -gt 3 ];then
	echo "ok";else
	echo "no"
fi
