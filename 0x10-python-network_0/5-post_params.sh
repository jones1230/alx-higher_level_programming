#!/bin/bash
# This script takes in URL, sends a POST request to the passed URL, and displays the body of response
curl -s "$1" -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD"
