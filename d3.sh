# 100 for loop
for i in $(seq 1 100)
do
    firefox d3-server.local &
    sleep 30
    pkill -f firefox
    echo $i
done