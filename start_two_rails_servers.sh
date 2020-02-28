#!/bin/bash

# TODO:
# Right now this script does not work.

# Path to rails project:
proj_path=$1

cd $proj_path

# I.E.: /Users/my.name/.rvm/gems/ruby-2.3.4@my-proj/bin/rails
$rvm_version_path=$2

full_path1="$rvm_version_path s -b localhost -e development -p 2000 -P $proj_path/tmp/pids/srv1.pid &"
full_path2="$rvm_version_path s -b localhost -e development -p 3000 -P $proj_path/tmp/pids/srv2.pid &"

$full_path1
$full_path2