#!/bin/bash
( echo "PACKAGE SIZE(M)";
for A in /var/lib/pacman/local/*/desc; do
  egrep -A1 '%(NAME|SIZE)' $A  \
   | gawk '/^[a-z]/ { printf "%s ", $1 }; /^[0-9]/ { printf "%.0f\n", $1/1048576 }'
done | sort -nrk2 ) | column -t | less

