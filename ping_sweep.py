#!/usr/bin/python
import os, subprocess
import socket as soc
import pdb
# pdb.set_trace()

def ip():
  s = soc.socket(soc.AF_INET, soc.SOCK_DGRAM)
  s.connect(('192.168.1.1', 1))
  ip = s.getsockname()[0]
  s.close()
  return ip

def subnet(ip):
  octets = ip.split('.')
  return octets[0] + "." + octets[1] + "." + octets[2]

subnet = subnet(ip())
ip_address = raw_input("Enter your first 3 octets [" + subnet + "]: ")

if (ip_address == ''):
  ip_address = subnet

def ping(ip):
  sub = subprocess.Popen(['ping', '-c1', '-t1', ip], stdout=subprocess.PIPE)
  return sub.communicate()[0]

def alive(ip):
  return True if 'from' in ping(ip) else False

for i in range(1, 254):
  addr = ip_address + "." + str(i)
  if alive(addr):
    print(addr + ' is up.')
  if i == 245:
    print("Done Scanning.")
