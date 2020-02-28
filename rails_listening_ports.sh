#!/bin/bash

netstat -na | grep -i LISTEN | grep '3000\|2000'
