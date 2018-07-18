ifconfig -a |  egrep '\binet [0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}.[0-9]{1,3}\b' | grep -v 127 | cut -f 2 -d" "
