if [ -z $2 ]; then 
	extension="$(echo $1 | grep -o '[^.]*$')"
	n=0	
	while [ stat compressed$n.$extension ]; do
		((i++))
	done
	outputfile="compressed$n.$extension"
else
	outputfile="$2"
fi
ffmpeg -i $1 -map 0:a:0 -b:a 96k $outputfile
