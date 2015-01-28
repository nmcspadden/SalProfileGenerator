#!/bin/bash

oldIFS="$IFS"
IFS=$'\n'
results=$( echo "SELECT key FROM server_machinegroup;" | python /home/docker/sal/manage.py dbshell | xargs | awk {'for (i=3; i<NF-1; i++) print $i'} )
read -rd '' -a lines <<<"$results"
for line in "${lines[@]}"
do
	if [[ -z $1 ]]; then
		"${BASH_SOURCE[0]}"/generate_sal_profile.py $line
	else
		"${BASH_SOURCE[0]}"/generate_sal_profile.py $line --url $1
	fi
done