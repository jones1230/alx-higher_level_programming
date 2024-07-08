#!/bin/bash
#This script diplays the Allowed methods of the server
curl -sI "$1" | grep "Allow" | cut -d' ' -f 2-
