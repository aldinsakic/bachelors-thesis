function onLoad(p) {
    // get the time for start of filtration.
    localStorage.setItem("filterStartTime", localStorage.getItem("filterStartTime")+', '+Date.now ())
    Plotly.d3.csv("https://raw.githubusercontent.com/aldinsakic/bachelors-thesis/main/standardDateGEI.csv", function (allData) {
        var xValues = Array.from(allData.filter(function (d) { return p.indexOf(d.group) >= 0 }).map(d => d.group));
        var yValues = Array.from(allData.map(d => d.variable));
        var zValues = Array.from(allData.filter(function (d) { return p.indexOf(d.group) >= 0 }).map(d => d.value));

        var data = [{
            x: xValues,
            y: yValues,
            z: zValues,
            type: 'heatmap',
            colorscale: 'Viridis',
            showscale: false,
        }];

        var layout = {
            title: 'GEI in EU across all avaliable years, interactive heatmap',
            autosize: true,
            height: 800,
            width: 800,
            automargin: false,
        };
        Plotly.newPlot('viz', data, layout, { displayModeBar: false })
    })
    // get the time for end of filtration.
    localStorage.setItem("filterEndTime", localStorage.getItem("filterEndTime")+', '+Date.now ())
}
