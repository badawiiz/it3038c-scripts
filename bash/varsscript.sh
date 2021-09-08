#!/bin/bash

a=$(ip a | grep 'noprefixroute ens192' | awk '{print $2}')
echo My IP is $a
echo Machine Type: $MACHTYPE
echo Hostname: $HOSTNAME
echo Working Dir: $PWD
echo Session Length: $SECONDS
echo Home Dir: $HOME
