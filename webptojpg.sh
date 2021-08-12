for x in $(ls *.webp | sed "s/.webp//g"); do
	convert $x.webp $x.jpg && rm $x.webp
done
