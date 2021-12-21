#!/bin/bash

IFS=$'\n'

echo "Enter remote branch [master]: "
read remote_branch

if [ "$remote_branch" == "" ]; then
  remote_branch="master"
fi

echo "Enter branch name: "
read branch_name

git checkout $remote_branch && git pull && git checkout -b $branch_name && git push -u origin $branch_name