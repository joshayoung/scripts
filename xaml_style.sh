#!/bin/bash

echo "Input Project Path (ie: ./MyProject)"

read project

~/.dotnet/tools/xstyler -d $project -c ./Settings.XamlStyler -r