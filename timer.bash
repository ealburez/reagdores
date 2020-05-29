#!/bin/bash

timeat="$1"
duration="$2"
ledpin="$3"

endtime=`date +%H:%M -d " $timeat today + $duration"`

gpio -g mode $ledpin out
echo "gpio -g write $ledpin 1" | at $timeat
echo "gpio -g write $ledpin 0" | at $endtime