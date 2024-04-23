# 200 for loop
for i in $(seq 1 200)
do
    firefox -no-remote plotly-server.local &
    sleep 5
done