#!/bin/bash
echo -n "sec:"
read sec
if [ $(($sec%2)) -lt 0 ]
   then
        echo "Secilen sayi tek basamakli"
   else
        echo "Secilen sayi cift basamakli"
fi

