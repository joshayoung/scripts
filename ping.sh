#!/bin/bash

ip=$1
for i in `seq 0 1 255`; do
    ping -c 3 -t 5 $ip.$i > /dev/null 2>&1 && echo $ip.$i is up;
done
