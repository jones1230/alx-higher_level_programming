#!/bin/bash
#This script rakes in a host:port and returns the content length of the curled page
curl -sI "$1" | grep 'Content-Length' | cut -d' ' -f2
