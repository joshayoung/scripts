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

echo "Select stash to restore, [c] to clear all stashes, or [n] to exit."

read number

if [ $number == "c" ]; then
  echo "You are about to remove all of your stashes, are you sure? [y, n]."
  read confirm
  if [ $confirm != "y" ]; then
    exit 0
  fi

  clear_stashes=$(git stash clear)
  ${clear_stashes}
  exit 0
fi

if [ $number == "n" ]; then
  exit 0
fi

number=$((number - 1))

git stash apply stash@{$number}