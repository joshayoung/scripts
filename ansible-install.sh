#!/bin/bash

echo "Install pip"
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py --user

echo "Install ansible"
python -m pip install --user ansible