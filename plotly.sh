# 200 for loop
for i in $(seq 1 200)
do
    echo "start"
    echo $i
    firefox -no-remote plotly-server.local &
    echo "sleeping"
    sleep 10
    echo "killing"
    #kill `pgrep "firefox"`
    pkill -f firefox
done