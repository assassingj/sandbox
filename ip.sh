#!/bin/bash


DIR=$(dirname $0)
cd $DIR
BASE=`pwd`
ifconfig | grep  inet | head -1 | awk '{print $2}' | awk -F: '{print $2}' > $BASE/ip.txt

echo $BASE
cd $BASE
git commit -m "new ip at `date`"
git push origin
