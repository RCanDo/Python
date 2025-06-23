#!/bin/bash
launch_as(){
	local cmd_name=$1
	shift
	"$@" > "$cmd_name.txt" 2>&1
	if [[ $? != 0 ]]; then
		echo "$cmd_name" >> fail.txt
	fi
}
launch_as mypy-strict mypy --strict app/ &
launch_as mypy-general mypy . &
wait
cat mypy-strict.txt
cat mypy-general.txt
if [[ -f fail.txt ]]; then
	cat fail.txt
	exit 1
fi

