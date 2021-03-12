#!/bin/bash
echo "Enter Container Name: "
read cont
echo "Enter Path to sqlite file inside your container: "
read sqlite_path
docker cp $cont:$sqlite_path ./
sqlite_file=`basename "$sqlite_path" `
backup_file=backup-$(date +'%m-%d-%Y').sql
touch $backup_file
sqlite3 $sqlite_file .dump > $backup_file
