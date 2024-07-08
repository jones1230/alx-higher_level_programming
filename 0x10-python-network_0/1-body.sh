#!/bin/bash
# This script takes in a URL and sends a GET request to the URL and displays the homepage
curl -s "$1" -X GET -L
