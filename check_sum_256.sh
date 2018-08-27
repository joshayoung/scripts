#!/bin/bash

valid_sum=$2
check_sum=`shasum -a 256 $1 | cut -d" " -f1`

if [ $check_sum = $valid_sum ]; then
  echo 'VALID Checksum!'
else
  echo 'INVALID!!'
fi


