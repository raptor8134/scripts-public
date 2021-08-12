bluetoothctl remove 1C:52:16:6A:7B:AA
while
	bluetoothctl pair 1C:52:16:6A:7B:AA >/dev/null
	[ $? == 1 ]
do :; done
bluetoothctl connect 1C:52:16:6A:7B:AA
