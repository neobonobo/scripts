count=0
while [ true ]; do
    filename=pi2_$(date +"%m%d%y_%Hh%Mm%Ss").jpg
    ssh pi@192.168.1.103 "raspistill -t 100 -ex auto -vf -hf -w 1280 -h 960 -q 10 -o $filename "
	sleep 4
	count=count+1
    echo $count
done;
