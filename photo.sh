filename=pi$(date +"%m-%d-%y-%Hh%Mm%Ss").jpg
echo "Capturing $filename"
raspistill -t 3000 -ss $1 -vf -hf -awb 'sun' -w 1280 -h 960 -o $filename
echo "Captured, now sending to you.."
scp $filename debi@192.168.1.110:/Users/debi/
sleep 1
echo "Deleting file on pi.."
rm $filename
echo "now opening the pic"
ssh debi@192.168.1.110 "open $filename "
