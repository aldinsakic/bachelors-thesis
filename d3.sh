# 200 for loop
for i in $(seq 1 200)
do
    firefox -no-remote d3-server.local &
    sleep 30
    pkill -f firefox
    echo $i
done