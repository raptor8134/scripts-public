# from https://jianmin.dev/2020/jul/19/boot-your-windows-partition-from-linux-using-kvm/
# do `sudo losetup -D` to detach all existing loop devices

ARR_DEV="/dev/md0"
WIN_PART="/dev/nvme0n1p4"
if [[ "$1" == "--stop" ]]; then
	sudo mdadm --stop $ARR_DEV
else
	sudo umount $WIN_PART
	sudo losetup -D
	sudo modprobe loop
	sudo modprobe linear
	LOOP1=$(sudo losetup -f)
	sudo losetup ${LOOP1} /var/lib/libvirt/images/efi1
	LOOP2=$(sudo losetup -f)
	sudo losetup ${LOOP2} /var/lib/libvirt/images/efi2
	sudo mdadm --build $ARR_DEV --chunk=512 --level=linear --raid-devices=3 \
   	${LOOP1} /dev/nvme0n1p4 ${LOOP2} --verbose
fi
