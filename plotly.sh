# 100 for loop
for i in $(seq 1 100)
do
    firefox 192.168.1.229 &
    sleep 30
    echo $i
done