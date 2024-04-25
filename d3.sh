# 100 for loop
for i in $(seq 1 100)
do
    firefox 192.168.1.112 &
    sleep 15
    echo $i
done