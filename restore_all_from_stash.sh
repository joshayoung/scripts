#!/bin/bash

###################################################################
# This allows you to more easily restore a stashed set of changes.
# This script could be cleaned up to make it less verbose.
###################################################################

IFS=$'\n'
all=$(git --no-pager stash list |cut -d$' ' -f2-)
all_values=($all)

count=1
for i in "${all_values[@]}"
do
  echo $count: $i
  count=$((count + 1))
done

echo "Select stash to restore"

read number

number=$((number - 1))
echo $number

git stash apply stash@{$number}