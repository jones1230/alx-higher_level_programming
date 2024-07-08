#!/bin/bash
#This script sends a GET request to the URL and displays the body
curl -s "$1" -X GET -H "X-School-User-Id: 98"
