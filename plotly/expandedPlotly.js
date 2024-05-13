var i = 0;
var filters = [['BE'], ['FI'], ['FI', 'DK'], ['BE', 'DK'], ['BE', 'DK', 'SE', 'IT'], ['FI', 'DK', 'SE', 'IT']];
function onLoad(p) {
    Plotly.d3.csv("https://raw.githubusercontent.com/aldinsakic/bachelors-thesis/main/expandedGEIYearsAndMonths.csv", function (allData) {
        // get the time for start of filtration.
        localStorage.setItem("filterStartTime", localStorage.getItem("filterStartTime") + ', ' + Date.now())
        var myPlot = document.getElementById('viz'),
            // d3 = Plotly.d3,
            layout = {
                title: 'GEI in EU across all avaliable years, interactive heatmap',
                autosize: true,
                height: 800,
                width: 800,
                automargin: false,
            },
            xValues = Array.from(allData.filter(function (d) { return p.indexOf(d.group) >= 0 }).map(d => d.group)),
            yValues = Array.from(allData.map(d => d.variable)),
            zValues = Array.from(allData.filter(function (d) { return p.indexOf(d.group) >= 0 }).map(d => d.value)),
            data = [{
                x: xValues,
                y: yValues,
                z: zValues,
                type: 'heatmap',
                colorscale: 'Viridis',
                showscale: false,
            }];

        Plotly.newPlot('viz', data, layout, { displayModeBar: false }).then(function () {
            // 5 frame buffer to confirm the visualisation is visible before measuring end of time.
            window.requestAnimationFrame(function () {
                window.requestAnimationFrame(function () {
                    window.requestAnimationFrame(function () {
                        window.requestAnimationFrame(function () {
                            window.requestAnimationFrame(function () {
                                localStorage.setItem("filterEndTime", localStorage.getItem("filterEndTime") + ', ' + Date.now())
                                if (i < filters.length) {
                                    onLoad(filters[i])
                                }
                                else {
                                    window.close();
                                }
                            });
                        });
                    });
                });
            });
        });
    })
    i++;
}