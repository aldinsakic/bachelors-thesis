function onLoad() {
    Plotly.d3.csv("https://raw.githubusercontent.com/aldinsakic/bachelors-thesis/main/GEI.csv", function(allData){

        // console.log(allData);

        // var xValues = ['A', 'B', 'C', 'D', 'E'];

        // var yValues = ['W', 'X', 'Y', 'Z'];

        // var zValues = [
        // [0.00, 0.00, 0.75, 0.75, 0.00],
        // [0.00, 0.00, 0.75, 0.75, 0.00],
        // [0.75, 0.75, 0.75, 0.75, 0.75],
        // [0.00, 0.00, 0.00, 0.75, 0.00]
        // ];
        var xValues = new Array();
        var yValues = new Array();
        // var xValues = ["2013", "2015", "2017", "2019", "2020", "2021", "2022", "2023"];
        // var yValues = ["BE","BG","CZ","DK","DE","EE","IE","EL","ES","FR","HR","IT","CY","LV","LT","LU","HU","MT","NL","AT","PL","PT","RO","SI","SK","FI","SE"];
        var zValues = new Array();
        for (var i=0; i<allData.length; i++) {
            row = allData[i];
            // console.log(row);
            xValues.push(row['group']);
            yValues.push(row['variable']);
            // zValues.push(Array.of(row['group'], row['variable'], row['value'],));
            zValues.push(row['value']);
            // console.log(xValues, yValues, zValues);
          }
          console.log(xValues, yValues, zValues);

        // var colorscaleValue = ['Viridis'];

        var data = [{
            x: xValues,
            y: yValues,
            z: zValues,
            type: 'heatmap',
            colorscale: 'Viridis',
            showscale: true,
            // transforms: [{
            //     type: 'filter',
            //     target: 'yValues',
            //     operation: '>',
            //     value: 3
            //   }]
        }];

        var layout = {
        title: 'GEI in EU across all avaliable years, interactive heatmap',
        // automargin: false,
        autosize: true,
        height: 500,
        width: 500,
        automargin: false,
        // xref: 10000,
        // update_layout: {yaxis_scaleanchor:"x"},
        // size:'dummy_column_for_size',
        // size_max:15,
        // margin: {
            //     dictt:100, b:0, l:80, r:0
            // },
            //annotations: [],
            // cells: {
            //     height: 10,
            //     width: 10,
            // },
            xaxis: {
                tickmode: 'linear',
                constrain: 'domain',
                //ticks: '',
                //ticksuffix: ' ',
                //width: 700,
                //height: 700,
                // autosize: true
            },
            yaxis: {
            //ticks: '',
            //ticksuffix: ' ',
            //width: 700,
            //height: 700,
            // autosize: true
            }
        };

        // for ( var i = 0; i < yValues.length; i++ ) {
        // for ( var j = 0; j < xValues.length; j++ ) {
        //     var currentValue = zValues[i][j];
        //     if (currentValue != 0.0) {
        //     var textColor = 'white';
        //     }else{
        //     var textColor = 'black';
        //     }
        //     var result = {
        //     xref: 'x1',
        //     yref: 'y1',
        //     x: xValues[j],
        //     y: yValues[i],
        //     text: zValues[i][j],
        //     font: {
        //         family: 'Arial',
        //         size: 12,
        //         color: 'rgb(50, 171, 96)'
        //     },
        //     showarrow: false,
        //     font: {
        //         color: textColor
        //     }
        //     };
        //     layout.annotations.push(result);
        // }
        // }

        Plotly.newPlot('viz', data, layout);
    })
}
