# 200 for loop
for i in $(seq 1 200)
do
    firefox -no-remote plotly-server.local &
    sleep 10
    pkill -f firefox
    echo $i
done