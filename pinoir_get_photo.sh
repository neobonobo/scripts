echo 'Capturing picture ...'
filename=pinoir$(date +"%m-%d-%y-%Hh%Mm%Ss").jpg
ssh pi@192.168.0.104 "raspistill -ex auto -t 100 -vf -hf -n -w 1280 -h 960 -q 10 -o '$filename' "
scp  pi@192.168.0.104:/home/pi/"$filename" ~/Pictures/MobileCamPhotos/
