#!/bin/bash


DIR=$(dirname $0)
ifconfig | grep  inet | head -1 | awk '{print $2}' | awk -F: '{print $2}' > $DIR/ip.txt
