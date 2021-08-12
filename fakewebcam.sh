NAME="fake webcam"
INPUT="$1"

if [[ "$(lsmod | grep v4l2loopback)" == "" ]]; then
	sudo modprobe v4l2loopback card_label="$NAME" exclusive_caps=1
fi

ffmpeg -stream_loop -1 -re -i $INPUT -vcodec rawvideo -threads 0 -f v4l2 /dev/video2
