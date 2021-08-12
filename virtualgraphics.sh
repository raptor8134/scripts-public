# kernel module config is at /etc/modprobe.d/GVT-g.conf and /etc/modules.d/GVT-g.conf
# https://wiki.archlinux.org/title/Intel_GVT-g

GVT_PCI="0000:00:02.0"
GVT_DOM="0000:00"

GVT_TYPE="i915-GVTg_V5_4"
GVT_GUID_1="869a437e-2ec1-4ff0-94b8-bcf359174136"
#GVT_GUID_2="40b25335-8173-4200-a4f6-f69756dd636f"
#GVT_GUID_3="b2f37f24-fe72-4592-b4d4-f67158bb3c97"

#ls /sys/class/mdev_bus/$GVT_PCI/mdev_supported_types

GVT_GUIDS="$GVT_GUID_1 $GVT_GUID_2 $GVT_GUID_3"
for GUID in $GVT_GUIDS; do
	if [[ "$1" == "--remove" ]]; then
		sudo bash -c 'echo 1 > /sys/bus/pci/devices/'$GVT_PCI'/'$GUID'/remove'
	else
		sudo bash -c 'echo "'$GUID'" > "/sys/class/mdev_bus/'$GVT_PCI'/mdev_supported_types/'$GVT_TYPE'/create"'
	fi
done

