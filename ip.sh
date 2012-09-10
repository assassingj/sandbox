#!/bin/bash


cd "`dirname $0`"
BASE=`pwd`
ifconfig | grep  -A1 eth0 | tail -1 | awk '{print $2}' | awk -F: '{print $2}' > $BASE/ip.txt

echo $BASE
cd $BASE
git add .
git commit -m "new ip at `date`"
git push origin
