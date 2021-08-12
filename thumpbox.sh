#bluetoothctl remove E8:07:BF:11:7D:EF
while
	bluetoothctl pair E8:07:BF:11:7D:EF >/dev/null
	[ $? -ne 0 ]
do :; done
bluetoothctl connect E8:07:BF:11:7D:EF
