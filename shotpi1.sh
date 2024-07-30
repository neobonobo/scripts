echo 'Capturing picture ...'
filename=pinoir_shot$(date +"%s").jpg
ssh pi@192.168.1.110 "raspistill -ex night -t 1000 -vf -hf -n -w 1280 -h 960 -q 10 -o '$filename' "
ssh -X pi@192.168.1.110 "gpicview $filename"
echo press any key to exit, x to delete 
read myvar
if [ $myvar = 'x' ]
then
ssh  pi@192.168.1.110 "rm $filename" 
fi

