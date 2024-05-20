#!/bin/sh -l

who_to_greet=$1
echo "Hello $who_to_greet"
time=$(date)
echo "time=$time" >> $GITHUB_OUTPUT