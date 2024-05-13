# 1000 for loop
for i in $(seq 1 1000)
do
    firefox 192.168.1.229/expandedPlotly.html &
    sleep 15
    echo $i plotly expand
done