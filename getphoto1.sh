#!/usr/local/bin/bash
echo 'where:'
echo "
	1.Pi3
	2.Pi4
	3.Quit
"
read pi_number
case $pi_number in
1) filename=pi3_$(date +"%m-%d-%y-%Hh%Mm%Ss").jpg
echo 'Capturing picture ...'
ssh debi@192.168.1.103 "raspistill -ex auto -t 50 -n -w 1280 -h 960 -q 30 -o '$filename' "
sleep 2
scp  debi@192.168.1.103:/home/debi/"$filename" ~/Pictures/MobileCamPhotos/pi3 
imgcat --height 15 ~/Pictures/MobileCamPhotos/pi3/"$filename"
echo "Press [enter] key to continue. . .";
read enterKey;;

2) filename=pi4_$(date +"%m-%d-%y-%Hh%Mm%Ss").jpg
echo 'Capturing picture ...'
ssh debi@88.255.60.151 "raspistill -vf -hf -ex auto -t 50 -n -w 1280 -h 960 -q 30 -o '$filename' "
sleep 2
scp  debi@88.255.60.151:/home/debi/"$filename" ~/Pictures/MobileCamPhotos/tarla
imgcat --height 15 ~/Pictures/MobileCamPhotos/tarla/"$filename";;
3) exit;; 
*)echo "Sorry, invalid choice, try again";;
esac
