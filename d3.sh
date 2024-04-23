# 200 for loop
for i in $(seq 1 200);
do
    firefox d3-server.local;
    sleep 10;
    kill `pgrep "firefox"`;
done