DEVICES=0
for x in $(bluetoothctl paired-devices | cut -f 2 -d " "); do
   	state="$(bluetoothctl info $x | grep Connected | cut -f 2 -d " ")"
   	if [[ "$state" == "yes" ]]; then
		if [[ "$1" == "--device" ]]; then
			echo $x
		else
			bluetoothctl info $x | head -n 2 | tail -n 1 | cut -f 2- -d " "
		fi
		DEVICES=+1
	fi
done
if [ $DEVICES -eq 0 ]; then 
	echo "No devices"
fi
