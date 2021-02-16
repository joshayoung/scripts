#!/bin/bash
dig -t "TXT" $1 | grep "TXT" | cut -f6 | sed -ne '3p'
