# 500 for loop
for i in $(seq 1 500)
do
    firefox 192.168.1.229/expandedPlotly.html &
    sleep 15
    echo $i plotly expand
done