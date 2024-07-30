while [ true ]; do
    echo 'Capturing picture ...'
    filename=salon_$(date +"%m-%d-%y-%Hh%Mm%Ss").jpg
    ssh pi@192.168.1.102 "raspistill -t 1000 -ex night -vf -hf -o '$filename' "
    printf "Downloading..\n"
    scp  pi@192.168.1.102:/home/pi/"$filename" ~/Pictures/SalonSinema/
    sleep 2
    #ssh pi@192.168.1.102 "rm  /home/pi/$filename"
    sleep 2
    printf "%10.16s  %0.20s\nQuitting..\n" "Deleting from pi" "$filename" 
    echo Done
done;
