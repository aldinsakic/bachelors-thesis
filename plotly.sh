# 100 for loop
for i in $(seq 1 100)
do
    firefox plotly-server.local &
    sleep 30
    pkill -f firefox
    echo $i
done