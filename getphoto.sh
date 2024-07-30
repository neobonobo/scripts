echo "raspistill parameters : "
#echo "enter value for -t --time : "
#read time
echo "enter value for -ss parameter : "
read shutter
ssh pi@192.168.0.104 "bash photo.sh $shutter"

