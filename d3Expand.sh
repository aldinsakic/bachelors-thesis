# 500 for loop
for i in $(seq 1 500)
do
    firefox 192.168.1.112/expandedD3.html &
    sleep 15
    echo $i d3 expand
done