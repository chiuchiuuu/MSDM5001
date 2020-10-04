#!/bin/bash
for i in $(seq 1 100)
do
    mkdir "DDM${i}"
    text="nanoseconds since 1970-01-01 00:00:00 UTC:\n"$(date "+%s%N")
    echo $text > "DDM${i}/time_till_now.txt"
done